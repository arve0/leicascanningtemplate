"""
Tests for `ScanningTemplate` class.
"""
import pytest
from lxml import objectify
from py import path
from leicascanningtemplate import ScanningTemplate


@pytest.fixture
def tmpl(tmpdir):
    "'base.xml' in tmpdir. Returns ScanningTemplate object"
    b = path.local(__file__).dirpath().join('base.xml')
    b.copy(tmpdir)

    return ScanningTemplate(tmpdir.join('base.xml').strpath)


def test_properties(tmpl):
    "ScanningTemplate should have tree, root and properties"
    assert isinstance(tmpl.root, objectify.ObjectifiedElement)
    assert isinstance(tmpl.properties, objectify.ObjectifiedElement)


def test_save_time(tmpl, tmpdir):
    "Saving should update time"
    original_date = tmpl.properties.CurrentDate
    out = tmpdir.join('out.xml').strpath
    tmpl.write(out)
    out_tmpl = ScanningTemplate(out)

    # time updated
    assert original_date != tmpl.properties.CurrentDate
    # time saved
    assert tmpl.properties.CurrentDate == out_tmpl.properties.CurrentDate


def test_save_start_position(tmpl, tmpdir):
    "Saving should start position if first field changed"
    orig_x = tmpl.properties.ScanFieldStageStartPositionX
    orig_y = tmpl.properties.ScanFieldStageStartPositionY

    new_x = 0.112233
    new_y = 0.332211

    tmpl.field_array.ScanFieldData.FieldXCoordinate = new_x
    tmpl.field_array.ScanFieldData.FieldYCoordinate = new_y

    out = tmpdir.join('out.xml').strpath
    tmpl.write(out)

    saved_x = tmpl.properties.ScanFieldStageStartPositionX
    saved_y = tmpl.properties.ScanFieldStageStartPositionY

    # start pos updated
    assert (orig_x, orig_y) != (saved_x, saved_y)
    # should be in microns
    assert saved_x == new_x * 1e6
    assert saved_y == new_y * 1e6


def test_update_well_positions(tmpl, tmpdir):
    """``update_well_positions`` should set
    ``ScanWellData.attrib['FieldXCoordinate']``
    """
    new_x = 0.0000112233
    new_y = 0.0000332211
    orig_x = tmpl.well_attrib()['FieldXStartCoordinate']
    orig_y = tmpl.well_attrib()['FieldYStartCoordinate']

    tmpl.well_fields()[0].FieldXCoordinate = new_x
    tmpl.well_fields()[0].FieldYCoordinate = new_y

    tmpl.update_well_positions()

    assert orig_x != tmpl.well_attrib()['FieldXStartCoordinate']
    assert orig_y != tmpl.well_attrib()['FieldYStartCoordinate']


def test_update_counts(tmpl, tmpdir):
    "Counts should update upon saving XML."
    # remove last well
    tmpl.remove_well(3, 1)

    # properties.CountOfWellsX not updated yet
    count_x = tmpl.count_of_wells[0]
    assert count_x == (tmpl.properties.CountOfWellsX - 1)

    # save and make sure count is updated
    out = tmpdir.join('out.xml').strpath
    tmpl.write(out)
    out_tmpl = ScanningTemplate(out)

    assert count_x == out_tmpl.properties.CountOfWellsX
