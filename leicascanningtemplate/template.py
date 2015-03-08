import time
from lxml import objectify, etree
from copy import deepcopy

class ScanningTemplate(object):
    """Python object of Leica LAS Matrix Screener Scanning Template XML.
    Provides easy access to elements via attributes:

        tmpl = ScanningTemplate('{ScanningTemplate}tmpl.xml')
        # attributes of MatrixScreenerTemplate/ScanningTemplate/Properties
        print(tmpl.properties.attrib)

    Parameters
    ----------
    filename : str
        XML to load.

    Attributes
    ----------
    root : lxml.objectify.ObjectifiedElement
        Objectified root of loaded XML.
        See http://lxml.de/objectify.html#the-lxml-objectify-api
    """
    def __init__(self, filename):
        self.filename = filename
        tree = objectify.parse(filename)
        self.root = tree.getroot()

    @property
    def properties(self):
        "Short hand for ``self.root.ScanningTemplate.Properties``"
        return self.root.ScanningTemplate.Properties

    # WELLS
    @property
    def well_array(self):
        "Short hand for ``self.root.ScanWellArray``"
        return self.root.ScanWellArray

    @property
    def wells(self):
        """All ScanWellData elements.

        Returns
        -------
        list of objectify.ObjectifiedElement
        """
        try:
            return self.root.ScanWellArray.ScanWellData[:]
        except AttributeError:
            return []

    def well_fields(self, well_x=1, well_y=1):
        """All ScanFieldData elements of given well.

        Parameters
        ----------
        well_x : int
        well_y : int

        Returns
        -------
        list of lxml.objectify.ObjectifiedElement
            All ScanFieldData elements of given well.
        """
        xpath = './ScanFieldArray/ScanFieldData'
        xpath += _xpath_attrib('WellX', well_x)
        xpath += _xpath_attrib('WellY', well_y)
        return self.root.findall(xpath)

    def well(self, well_x=1, well_y=1):
        """ScanWellData of specific well.

        Parameters
        ----------
        well_x : int
        well_y : int

        Returns
        -------
        lxml.objectify.ObjectifiedElement
        """
        xpath = './ScanWellData'
        xpath += _xpath_attrib('WellX', well_x)
        xpath += _xpath_attrib('WellY', well_y)
        # assume we find only one
        return self.well_array.find(xpath)


    def well_attrib(self, well_x=1, well_y=1):
        """Attributes of specific well.

        Parameters
        ----------
        well_x : int
        well_y : int

        Returns
        -------
        dict
            Attributes of ScanWellArray/ScanWellData.
        """
        return self.well(well_x, well_y).attrib

    # FIELDS
    @property
    def field_array(self):
        "Short hand for ``self.root.ScanFieldArray``"
        return self.root.ScanFieldArray

    @property
    def fields(self):
        """All ScanFieldData elements.

        Returns
        -------
        list of objectify.ObjectifiedElement
        """
        try:
            return self.root.ScanFieldArray.ScanFieldData[:]
        except AttributeError:
            return []

    def field(self, well_x=1, well_y=1, field_x=1, field_y=1):
        """ScanFieldData of specified field.

        Parameters
        ----------
        well_x : int
        well_y : int
        field_x : int
        field_y : int

        Returns
        -------
        lxml.objectify.ObjectifiedElement
            ScanFieldArray/ScanFieldData element.
        """
        xpath = './ScanFieldArray/ScanFieldData'
        xpath += _xpath_attrib('WellX', well_x)
        xpath += _xpath_attrib('WellY', well_y)
        xpath += _xpath_attrib('FieldX', field_x)
        xpath += _xpath_attrib('FieldY', field_y)
        # assume we find only one
        return self.root.find(xpath)


    def update_start_position(self):
        "Set start position of experiment to position of first field."
        x_start = self.field_array.ScanFieldData.FieldXCoordinate
        y_start = self.field_array.ScanFieldData.FieldYCoordinate
        self.properties.ScanFieldStageStartPositionX = x_start * 1e6 # in um
        self.properties.ScanFieldStageStartPositionY = y_start * 1e6


    def update_well_positions(self):
        """Set ``well_attrib['FieldXStartCoordinate']`` and
        ``well_attrib['FieldYStartCoordinate']`` to FieldXCoordinate and
        FieldYCoordinate of first field in well.
        """
        for well in self.wells:
            well_x = well.attrib['WellX']
            well_y = well.attrib['WellY']

            first_field = self.well_fields(well_x, well_y)[0]

            x_start = first_field.FieldXCoordinate.text
            y_start = first_field.FieldYCoordinate.text

            well.attrib['FieldXStartCoordinate'] = x_start
            well.attrib['FieldYStartCoordinate'] = y_start


    @property
    def count_of_wells(self):
        """Number of wells in x/y-direction of template.

        Returns
        -------
        tuple
            (xs, ys) number of wells in x and y direction.
        """
        xs = set([w.attrib['WellX'] for w in self.wells])
        ys = set([w.attrib['WellY'] for w in self.wells])
        return (len(xs), len(ys))

    @property
    def count_of_assigned_jobs(self):
        "Number of fields that have attrib['JobAssigned'] set to true."
        assigned = len([x.attrib['JobAssigned'] for x in self.fields
                            if x.attrib['JobAssigned'] == 'true'])
        return assigned


    def update_counts(self):
        "Update counts of fields and wells."
        # Properties.attrib['TotalCountOfFields']
        fields = str(len(self.fields))
        self.properties.attrib['TotalCountOfFields'] = fields

        # Properties.CountOfWellsX/Y
        wx, wy = (str(x) for x in self.count_of_wells)

        self.properties.CountOfWellsX = wx
        self.properties.CountOfWellsY = wy

        # Properties.attrib['TotalCountOfWells']
        wells = str(len(self.wells))
        self.properties.attrib['TotalCountOfWells'] = wells

        # Properties.attrib['TotalAssignedJobs']
        self.properties.attrib['TotalAssignedJobs'] = str(self.count_of_assigned_jobs)


    def remove_well(self, well_x, well_y):
        """Remove well and associated scan fields.

        Parameters
        ----------
        well_x : int
        well_y : int

        Raises
        ------
        AttributeError
            If well not found.
        """
        well = self.well(well_x, well_y)
        if well == None:
            raise AttributeError('Well not found')
        self.well_array.remove(well)

        # remove associated fields
        fields = self.well_fields(well_x, well_y)
        for f in fields:
            self.field_array.remove(f)


    def well_exists(self, well_x, well_y):
        "Check if well exists in ScanWellArray."
        return self.well(well_x, well_y) != None


    def field_exists(self, well_x, well_y, field_x, field_y):
        "Check if field exists ScanFieldArray."
        return self.field(well_x, well_y, field_x, field_y) != None


    def add_well(self, well_x, well_y, start_x, start_y):
        """Add well with associated scan fields. ``self.wells[0]`` and
        ``self.fields[0]`` will be used as base. ScanWellData will be added to
        ScanWellArray and ScanFieldData to ScanFieldArray. The amount of fields
        added is decided by Properties/CountOfScanFields.

        Parameters
        ----------
        well_x : int
        well_y : int
        start_x : int
            In meters. FieldXCoordinate of first field in well.
        start_y : int
            In meters. FieldYCoordinate of first field in well.

        Raises
        ------
        ValueError
            If well or fields already exists.
        """
        # raise ValueError if well already exists
        if self.well_exists(well_x, well_y):
            raise ValueError('Well already exists in ScanWellArray')

        if len(self.well_fields(well_x, well_y)) != 0:
            raise ValueError('Fields belonging to well already exists in ScanFieldArray')

        base_well = deepcopy(self.wells[0])

        # append well to ScanWellArray
        base_well.attrib['WellX'] = str(well_x)
        base_well.attrib['WellY'] = str(well_y)
        self.well_array.append(base_well)

        # append fields to ScanFieldArray
        x_fields = int(self.properties.CountOfScanFieldsX)
        y_fields = int(self.properties.CountOfScanFieldsY)
        x_dist = float(self.properties.ScanFieldStageDistanceX) * 1e-6 # in um
        y_dist = float(self.properties.ScanFieldStageDistanceY) * 1e-6
        x_label = str(self.properties.TextWellPlateHorizontal[well_x - 1])
        y_label = str(self.properties.TextWellPlateVertical[well_y - 1])

        for i in range(x_fields):
            for j in range(y_fields):
                base_field = deepcopy(self.fields[0])

                base_field.FieldXCoordinate = start_x + i*x_dist
                base_field.FieldYCoordinate = start_y + j*y_dist

                base_field.attrib['WellX'] = str(well_x)
                base_field.attrib['WellY'] = str(well_y)

                base_field.attrib['FieldX'] = str(i+1)
                base_field.attrib['FieldY'] = str(j+1)

                base_field.attrib['LabelX'] = x_label
                base_field.attrib['LabelY'] = y_label

                self.field_array.append(base_field)


    def write(self, filename=None):
        """Save template to xml. Before saving template will update
        date, start position, well positions, and counts.

        Parameters
        ----------
        filename : str
            If not set, XML will be written to self.filename.
        """
        if not filename:
            filename = self.filename

        # update time
        self.properties.CurrentDate = _current_time()

        # update start position
        self.update_start_position()

        # update well postions
        self.update_well_positions()

        # update counts
        self.update_counts()

        with open(filename, 'wb') as f:
            # remove py:pytype attributes
            objectify.deannotate(self.root)

            # remove namespaces added by lxml
            for child in self.root.iterchildren():
                etree.cleanup_namespaces(child)

            xml = etree.tostring(self.root, encoding='utf8',
                                 xml_declaration=True, pretty_print=True)
            f.write(xml)


def _current_time():
    "Time formatted as `Monday, February 09, 2015 | 8:12 PM`"
    return time.strftime('%A, %B %d, %Y | %I:%M %p')

def _xpath_attrib(attrib, value):
    """Returns string ``[@attrib="value"]``.
    """
    return '[@' + str(attrib) + '="' + str(value) + '"]'
