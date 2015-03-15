# Scanning Template
Here is an overview of whats available in the scanning template:

- **Bold** is XML-elements.
- *Italics* is element attributes.
- (Examples of values) are inside ().

Element values can be retrieved by their name:
`tmpl.properties.ScanFieldStageDistanceX`

Attributes can be retrieved property `attrib` on the element:
`tmpl.properties.attrib`

Updating values:
- `tmpl.properties.ScanFieldStageDistanceX = 400`
- `tmpl.properties.attrib['TotalCountOfWells'] # automatic updated upon tmpl.write()`


## Properties
Xpath: `MatrixScreenerTemplate/ScanningTemplate/Properties`

Avialable through `ScanningTemplate(filename).properties`.

- *Version* (Version: 1.0.4.563 -- Build 08.08.2013)
- *TotalCountOfFields* (27)
- *TotalCountOfWells* (3)
- *TotalAssignedJobs* (27)
- *UniqueJobCounter* (1)
- **CurrentDate** (Monday, January 12, 2015 | 4:09 PM)
- **EnableTrigger** (false)
- **TriggerRepeatCycles** (1)
- **DriftScanRange** (80)
- **DriftSliceCount** (5)
- **EnableCAM** (true)
- **ShowPumpFields** (false)
- **EnablePump** (false)
- **PumpRepeatInterval** (1)
- **PumpDelay** (1000)
- **PumpTime** (1000)
- **EnableContextMenu** (true)
- **ContextType** (eMatrixContextStripe)
- **ScanningTemplateType** (eIsMatrixTemplate)
- **EnableTrackRemoveBoundaryObjects** (false)
- **EnableTrackRemoveSmallObjects** (false)
- **TrackAdaptiveThreshold** (3)
- **TrackSizeOfSmallObject** (15)
- **TrackRepeatInterval** (1)
- **ShowTrackingFields** (false)
- **EnableTracking** (false)
- **FixHeigthOfWell** (50)
- **FixWidthOfWell** (50)
- **HoldSize** (false)
- **TextColorHeatMapDescription** (808080)
- **DrawRandomizedTestHeatMap** (false)
- **EnableLUTBarInAgenda** (false)
- **LUTBarDescription** (Focus Map)
- **LUTBarUpperText** (-- 4009.7 µm)
- **LUTBarLowerText** (-- 4008.2 µm)
- **LUTBarInHeight** (144)
- **EnableHeatMap** (false)
- **HeatMapType** (IsFocusMap)
- **HeatMapLUT** (LUT_JET)
- **ColorWellOutlineSelected** (00FF00)
- **ColorInActiveScanField** (808080)
- **ColorScanFieldBoundary** (000000)
- **ColorScanFieldForTracking** (00FF00)
- **ColorCurrentScanField** (00FF00)
- **ColorActiveScanField** (404040)
- **ColorWellOutline** (000000)
- **ColorWellFilled** (23272E)
- **EnableMultiSelection** (false)
- **ColorSelectedFields** (9ACD32)
- **EnableRubberBand** (true)
- **ColorRubberBand** (C00000)
- **ScanFieldEffectDesign** (None)
- **ScanFieldShapeDesign** (IsRectangle)
- **ScanFieldDistanceX** (2)
- **ScanFieldDistanceY** (2)
- **ScanFieldDiameter** (40)
- **CountOfScanFieldsX** (3)
- **CountOfScanFieldsY** (3)
- **ExperimenTimeDistance** (15)
- **ExperimentLoopCount** (1)
- **EnableIndividualWellScanFieldCount** (false)
- **DrawWellOutlineIfSelected** (false)
- **DrawWellOutline** (true)
- **WellsDistanceX** (42)
- **WellsDistanceY** (42)
- **CountOfWellsX** (3)
- **CountOfWellsY** (1)
- **TextColorWellplateDescription** (808080)
- **TextWellPlateHorizontal** (A)
- **TextWellPlateHorizontal** (B)
- **TextWellPlateHorizontal** (C)
- **TextWellPlateHorizontal** (D)
- **TextWellPlateHorizontal** (E)
- **TextWellPlateHorizontal** (F)
- **TextWellPlateHorizontal** (G)
- **TextWellPlateHorizontal** (H)
- **TextWellPlateHorizontal** (I)
- **TextWellPlateHorizontal** (J)
- **TextWellPlateHorizontal** (K)
- **TextWellPlateHorizontal** (L)
- **TextWellPlateHorizontal** (M)
- **TextWellPlateHorizontal** (N)
- **TextWellPlateHorizontal** (O)
- **TextWellPlateHorizontal** (P)
- **TextWellPlateHorizontal** (Q)
- **TextWellPlateHorizontal** (R)
- **TextWellPlateHorizontal** (S)
- **TextWellPlateHorizontal** (T)
- **TextWellPlateHorizontal** (U)
- **TextWellPlateHorizontal** (V)
- **TextWellPlateHorizontal** (W)
- **TextWellPlateHorizontal** (X)
- **TextWellPlateHorizontal** (Y)
- **TextWellPlateHorizontal** (Z)
- **TextWellPlateHorizontal** (AA)
- **TextWellPlateHorizontal** (BB)
- **TextWellPlateHorizontal** (CC)
- **TextWellPlateHorizontal** (DD)
- **TextWellPlateHorizontal** (EE)
- **TextWellPlateHorizontal** (FF)
- **TextWellPlateHorizontal** (AB)
- **TextWellPlateHorizontal** (AC)
- **TextWellPlateHorizontal** (AD)
- **TextWellPlateHorizontal** (AE)
- **TextWellPlateHorizontal** (AF)
- **TextWellPlateVertical** (1)
- **TextWellPlateVertical** (2)
- **TextWellPlateVertical** (3)
- **TextWellPlateVertical** (4)
- **TextWellPlateVertical** (5)
- **TextWellPlateVertical** (6)
- **TextWellPlateVertical** (7)
- **TextWellPlateVertical** (8)
- **TextWellPlateVertical** (9)
- **TextWellPlateVertical** (10)
- **TextWellPlateVertical** (11)
- **TextWellPlateVertical** (12)
- **TextWellPlateVertical** (13)
- **TextWellPlateVertical** (14)
- **TextWellPlateVertical** (15)
- **TextWellPlateVertical** (16)
- **TextWellPlateVertical** (17)
- **TextWellPlateVertical** (18)
- **TextWellPlateVertical** (19)
- **TextWellPlateVertical** (20)
- **TextWellPlateVertical** (21)
- **TextWellPlateVertical** (22)
- **TextWellPlateVertical** (23)
- **TextWellPlateVertical** (24)
- **TextWellPlateVertical** (25)
- **TextWellPlateVertical** (26)
- **TextWellPlateVertical** (27)
- **TextWellPlateVertical** (28)
- **TextWellPlateVertical** (29)
- **TextWellPlateVertical** (30)
- **TextWellPlateVertical** (31)
- **TextWellPlateVertical** (32)
- **TextWellPlateVertical** (33)
- **TextWellPlateVertical** (34)
- **TextWellPlateVertical** (35)
- **TextWellPlateVertical** (36)
- **TextWellPlateVertical** (37)
- **TextWellPlateVertical** (38)
- **TextWellPlateVertical** (39)
- **TextWellPlateVertical** (40)
- **TextWellPlateVertical** (41)
- **TextWellPlateVertical** (42)
- **TextWellPlateVertical** (43)
- **TextWellPlateVertical** (44)
- **TextWellPlateVertical** (45)
- **TextWellPlateVertical** (46)
- **TextWellPlateVertical** (47)
- **TextWellPlateVertical** (48)
- **TextWellPlateVertical** (49)
- **TextWellPlateVertical** (50)
- **TextWellPlateVertical** (51)
- **TextWellPlateVertical** (52)
- **TextWellPlateVertical** (53)
- **TextWellPlateVertical** (54)
- **TextWellPlateVertical** (55)
- **TextWellPlateVertical** (56)
- **TextWellPlateVertical** (57)
- **TextWellPlateVertical** (58)
- **TextFillColorTextBox** (A5A6A1)
- **TextColorTextBox** (23272E)
- **EnableTextBox** (false)
- **TextFontSize** (12)
- **DrawText** (false)
- **FlipText** (false)
- **AgendaLineDistance** (30)
- **AgendaTextDistance** (20)
- **AgendaBulletWidth** (15)
- **AgendaTextWidth** (120)
- **AgendaXPosition** (20)
- **AgendaYPosition** (0)
- **AgendaTextColor** (D4D3CC)
- **AgendaFontSize** (10)
- **EnableAgenda** (true)
- **DescriptionTextColor** (000000)
- **DescriptionFontSize** (10)
- **EnableDescription** (true)
- **Description** ({ScanningTemplate}test CAM )
- **BlinkerColorOff** (006400)
- **BlinkerColorOn** (00FF00)
- **BlinkerIntervall** (500)
- **ColorDesign** (LeicaDesign)
- **ScanFieldStageStartPositionX** (39951.978260573691)
- **ScanFieldStageStartPositionY** (30174.394491387618)
- **ScanFieldStageDistanceX** (450)
- **ScanFieldStageDistanceY** (450)
- **ScanWellStageDistanceX** (1740)
- **ScanWellStageDistanceY** (1740)
- **ScanFieldArrayOffsetZ** (0)
- **AutoFocusPattern** (IsStandardAFScanFieldPattern)
- **AutoFocusColor** (FF7F50)
- **AutoFocusScanFieldInterval** (2)
- **AutoFocusScanRange** (5)
- **AutoFocusSliceCount** (10)
- **EnableAutoFocusDZOffset** (false)
- **AutoFocusDzOffset** (-0)
- **ZUseMode** (2)
- **DriftRepeatInterval** (1)
- **ShowDriftCompensationFields** (true)
- **PetriDishVisualisation** (false)
- **SelectedAutofocusJobName** (AF Job)
- **SelectedTrackJobName** (Job 2)
- **IsOverlapInPercentSelected** (true)
- **MosaicOverlapInPercent** (10)
- **MosaicOverlapInMicronsX** (0)
- **MosaicOverlapInMicronsY** (0)
- **CanDoRealTime3D** (false)
- **AutoRotate3D** (false)


## ScanFieldData
Xpath: `MatrixScreenerTemplate/ScanFieldArray/ScanFieldData`

Available through `tmpl.fields` and
`tmpl.field(well_x=1, well_y=1, field_x=1, field_y=1)`.

A field may be deleted from the ScanFieldArray like this:
`tmpl.field_array.remove(tmpl.field(1, 2, 3, 4))`

- *JobId* (8)
- *SlideNo* (0)
- *WellX* (1)
- *WellY* (1)
- *FieldX* (1)
- *FieldY* (1)
- *JobName* (Job 2)
- *Description* (MatrixScreener)
- *IsMosaicCalibrationField* (false)
- *IsDriftCompensationField* (false)
- *IsIndividualAutofocusScanField* (false)
- *IsTrackingField* (false)
- *IsPumpScanField* (false)
- *PumpDelay* (1000)
- *PumpTime* (1000)
- *Selected* (false)
- *Enabled* (true)
- *Indicator* (IsStandardScanField)
- *IsAutofocusScanField* (false)
- *AFScore* (0)
- *State* (IsActive)
- *AFJobId* (0)
- *AFSliceCount* (10)
- *DriftScanRange* (4.9999999999999996E-06)
- *DriftSliceCount* (5)
- *AFScanRange* (4.9999999999999996E-06)
- *Shape* (IsRectangle)
- *JobAssigned* (true)
- *LabelX* (A)
- *LabelY* (1)
- **FieldXCoordinate** (0.039951978260573694)
- **FieldYCoordinate** (0.030174394491387618)
- **FieldZCoordinate** (0.0040081944009173224)
- **FieldScanSlices** (0)
- **FieldScanRange** (0)
- **FieldRotation** (0)


## ScanWellData
Xpath: `MatrixScreenerTemplate/ScanWellArray/ScanWellData`

- *SlideNo* (1)
- *WellX* (1)
- *WellY* (1)
- *MosaicSingleImageHeight* (1)
- *MosaicTileImageOverlapX* (0)
- *MosaicTileImageOverlapY* (0)
- *MosaicScanImageRotation* (0)
- *MosaicSingleImageWidth* (1)
- *MosaicImageStartX* (0)
- *MosaicImageStartY* (0)
- *MosaicImageHeight* (0)
- *MosaicImageWidth* (0)
- *MosaicImageEndX* (0)
- *MosaicImageEndY* (0)
- *MosaicFlipImage* (false)
- *FieldXStartCoordinate* (0.039951978260573694)
- *FieldYStartCoordinate* (0.030174394491387618)
- *FieldZCoordinate* (0.0040081944009173224)
- *ScanFieldDiameter* (0)
- *WellXOffset* (0)
- *WellYOffset* (0)
- *XCountOfFields* (3)
- *YCountOfFields* (3)
- *Indicator* (IsStandardScanWell)