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

## Scan settings (found in .lrp)
Root is **Configuration**
- *Type* (7)
- *SystemType* (-1)
- *ID* (1339176636)
- **LDM_Block_Sequence**
  - *BlockName* (collecting pattern)
  - **LDM_Block_Sequence_Element_List**
    - **LDM_Block_Sequence_Element**
      - *BlockID* (12)
      - *ElementID* (1)
      - *LoopToNextElement* (0)
      - *LoopCount* (-1)
      - *RemainingLoopCount* (-1)
      - *PauseTime* (0)
      - *m_eInTrigger* (-1)
      - *m_eInTriggerShowInGraph* (1)
      - *m_eInTriggerRecordInEventlist* (1)
      - *m_eInTriggerDescription*
      - *WFInTriggerMode* (-1)
      - *m_eOutTrigger* (-1)
      - *m_eOutTriggerShowInGraph* (1)
      - *m_eOutTriggerRecordInEventlist* (1)
      - *m_eOutTriggerDescription*
      - *WFOutTriggerMode* (-1)
      - *m_eOutTriggerOnStart* (-1)
      - *m_eOutTriggerOnStartShowInGraph* (1)
      - *m_eOutTriggerOnStartRecordInEventlist* (1)
      - *m_eOutTriggerOnStartDescription*
      - *m_eOutTriggerOnEnd* (-1)
      - *m_eOutTriggerOnEndShowInGraph* (1)
      - *m_eOutTriggerOnEndRecordInEventlist* (1)
      - *m_eOutTriggerOnEndDescription*
      - *m_eOutTriggerOnDelay* (-1)
      - *m_eOutTriggerOnDelayShowInGraph* (1)
      - *m_eOutTriggerOnDelayRecordInEventlist* (1)
      - *m_eOutTriggerOnDelayDescription*
      - *WaitTimeBeforeDelayTriggerOut* (0)
      - *IsLoopActive* (0)
      - *AFLinkBlockID* (0)
      - *AF_LDM_Mode* (0)
      - *AF_Offset* (0)
      - *BlockType* (0)
- **LDM_Block_Sequence_Block_List**
  - **LDM_Block_Sequence_Block**
    - *BlockType* (0)
    - *BlockID* (12)
    - *BlockIsUsingCameraImageSource* (0)
    - **LDM_Block**
      - *BlockName* (AF Job)
      - **ATLConfocalSettingDefinition**
        - *VersionNumber* (8)
        - *UserSettingName* (S69)
        - *CanDoSTED* (0)
        - *IsSTEDActive* (0)
        - *UseSystemOptimizedVoxelCalculation* (1)
        - *STEDDelayTimeOffset* (0)
        - *STEDDelayTimeOffset2* (0)
        - *StedDelayWavelength* (470)
        - *IsUserSettingNameSet* (0)
        - *BitSize* (8)
        - *ScanMode* (xyz)
        - *ZUseMode* (1)
        - *ZUseModeName* (z-galvo)
        - *ZPosition* (-2.3841880645312E-10)
        - *IsSuperZ* (0)
        - *ValidBeginStack* (0)
        - *ValidEndStack* (0)
        - *Sections* (1)
        - *StackCalculationMode* (2)
        - *StackCalculationModeName* (System optimized step size)
        - *IsZStackAroundCurrent* (0)
        - *IsMPFormulaForStepSizerUsageActive* (0)
        - *IsFastZStack* (0)
        - *ZStackDirectionMode* (1)
        - *ZStackDirectionModeName* (Unidirectional)
        - *CycleCount* (1)
        - *CycleTime* (0)
        - *CompleteTime* (0.226333333333333)
        - *LineTime* (1.66666666666667E-03)
        - *FrameTime* (0.226333333333333)
        - *UseMaxIterationsForT* (0)
        - *IsTimeMinimizeEnabled* (0)
        - *LastTCalcMode* (3)
        - *Lines* (512)
        - *Pages* (1)
        - *MaxLines* (1)
        - *StagePosX* (0.08229879087081)
        - *StagePosY* (0.02928905726962)
        - *StageRangeX* (0.11279375084332)
        - *StageRangeY* (0.07937427088379)
        - *Magnification* (10)
        - *ObjectivePos* (2)
        - *CanDoOpticalZoom* (0)
        - *OpticalZoom* (1)
        - *ObjectiveName* (HC PL APO    10x/0.40 DRY )
        - *ObjectiveNumber* (11506511)
        - *MicroscopeModel* (DMI6000B-CS)
        - *IsInverseMicroscopeModel* (1)
        - *Immersion* (DRY)
        - *NumericalAperture* (0.4)
        - *RefractionIndex* (1)
        - *IsFCSFilterAutomationActive* (0)
        - *IsSMDChaserUVAOTFAutomationActive* (0)
        - *IsAutofocusOnStart* (1)
        - *AutofocusRedoEveryNTimePoints* (0)
        - *CanDoCSMode* (1)
        - *ActiveCS_SubModeForTLD* (0)
        - *ActiveCS_SubModeForTLDName* (Scan-BF)
        - *ActiveCS_SubModeForRLD* (0)
        - *ActiveCS_SubModeForRLDName* (Empty)
        - *LastNonMP_MFP_FW_Name* (Substrate )
        - *LastNonMP_Pol_FW_Name* (Empty)
        - *ScanSpeed* (600)
        - *InDimension* (128)
        - *OutDimension* (128)
        - *UseScanFormatRestriction* (0)
        - *Zoom* (0.75)
        - *BaseZoom* (0.75)
        - *PanFirstDim* (8.67361737988404E-19)
        - *PanSecondDim* (8.67361737988404E-19)
        - *ScanDirectionX* (1)
        - *ScanDirectionXName* (Unidirectional)
        - *RotatorAngle* (92.0004500450045)
        - *LambdaExcitationMode* (0)
        - *LambdaExcitationModeBegin* (0)
        - *LambdaExcitationModeEnd* (0)
        - *Pinhole* (5.30206177527711E-05)
        - *PinholeAiry* (0.999069488463747)
        - *EmissionWavelengthForPinholeAiryCalculation* (580)
        - *FrameAverage* (1)
        - *LineAverage* (1)
        - *FrameAccumulation* (1)
        - *Line_Accumulation* (1)
        - *AreBleachPointsEnabled* (0)
        - *InTrigger* (-1)
        - *OutTrigger* (-1)
        - *IsRoiScanEnable* (0)
        - *Is3DLimitedRoiScanEnable* (0)
        - *Limited3DRoiFirstSection* (1)
        - *Limited3DRoiLastSection* (1)
        - *ZCompensationModes* (0)
        - *ReferencePosition* (0)
        - *IsConstantIntegrationTimeActive* (1)
        - *PixelDwellTime* (0.00000325)
        - *SystemSerialNumber* (8100000303)
        - **EasySRMappingArray**
        - **EasySRSlider**
          - *SRRelative* (75)
          - *ThreeDRelative* (0)
          - *GentleRelative* (25)
        - **Quantity**
          - *Value* (0)
          - *Unit* (m)
        - **AdditionalZPositionList**
          - **AdditionalZPosition**
            - *Valid* (1)
            - *SuperZMode* (1)
            - *SuperZModeName* (RestrictedRange)
            - *ZMode* (1)
            - *ZUseModeName* (z-galvo)
            - *ZPosition* (-2.3841880645312E-10)
        - **Autofocus-config**
          - *VersionNumber* (1)
          - *Precision* (2)
          - *FocusRange* (0.00008)
          - *ZUseMode* (1)
          - *ZUseModeName* (z-galvo)
          - *AFAnalyseType* (1)
          - *AFAnalyseTypeName* (EveryChannel)
          - *WorkflowTimelapse* (1)
          - *WorkflowTimelapseName* (FirstTime)
          - *WorkflowTimelapseIterator* (1)
          - *WorkflowXY* (1)
          - *WorkflowXYName* (FirstPos)
          - *WorkflowXYIterator* (1)
          - *UseFixSliceNumber* (0)
          - *AFSubsystem* (3)
          - *AFSubsystemName* (CombinedConfocal)
          - *AFCOffset* (-2)
          - *AFCAutonomousOffset* (-2)
          - *AutoFocusMode* (2)
          - *AutoFocusModeName* (FirstChannelOnly)
          - *AutofocusChannel* (1)
          - *AutofocusChannelName* (1002)
          - *OptimalStepSize* (2.40796995428705E-06)
          - *PositionDimension* (122)
        - **ShutterList**
          - **Shutter**
            - *LightSourceQualifier* (70)
            - *ShutterQualifier* (8)
            - *LightSourceName* (SuperCont)
            - *ShutterName* (WLL)
            - *IsActive* (0)
        - **BleachPoints**
          - **LMSDataContainerHeader**
            - *Version* (2)
            - **Element**
              - *Name* (BleachPointROISet)
              - *Visibility* (2)
              - *CopyOption* (1)
              - *UniqueID* (83457453-b08e-11e4-8e53-bcf685d7650c)
              - **Data**
                - **ROISet**
                  - *ROISetType* (1)
                  - *PossibleChildROITypes* (-1)
                  - *PossibleROITransforms* (65535)
                  - *PossibleROIActions* (65535)
              - **Memory**
                - *Size* (0)
                - *MemoryBlockID* (MemBlock_203)
              - **Children**
        - **ATLConfocalBleachPointsSettings**
        - **FilterWheel**
          - *FluorifierAutoSelection* (1)
          - *BeamSplitterAutoSelection* (0)
          - *StedBeamSelectionPinholeCoupling* (0)
          - *MultiFunctionPortAutoSelection* (1)
          - **Wheel**
            - *Qualifier* (214)
            - *FilterWheelName* (Attenuation MP)
            - *LightSourceQualifier* (40)
            - *FilterIndex* (0)
            - *FilterName* (Min)
            - *IsSpectrumTurnMode* (1)
            - *FilterSpectrumPos* (49132)
            - *FilterSpectrumValue* (12.3719199833143)
            - *IndexChanged* (0)
            - *SpectrumChanged* (0)
            - **WheelName**
              - *FilterName* (Min)
        - **Spectro**
          - **MultiBand**
            - *Channel* (1)
            - *ChannelName* (Channel 1)
            - *LeftWorld* (380)
            - *RightWorld* (423.705785750378)
            - *DyeName*
        - **AotfList**
          - **Aotf**
            - *AotfQualifier* (90)
            - *AotfQualifierName* (WLL)
            - *LightSourceQualifier* (70)
            - *LightSourceQualifierName* (SuperCont)
            - *OpenVirtual* (0)
            - *IsChanged* (0)
            - *ExcitationControlMode* (0)
            - *ExcitationControlModeBegin* (0)
            - *ExcitationControlModeEnd* (0)
            - *CanDoPulseFreq* (0)
            - *PulsFreq* (0)
            - *CanDoTwoLaserPIE* (0)
            - *TwoLaserPIEPossibleLastState* (0)
            - *TwoLaserPIEActive* (0)
            - **LaserLineSetting**
              - *LaserLine* (470)
              - *IntensityDev* (0)
              - *IntensityLowDev* (0)
              - *AOBSIntensityDev* (-1)
              - *AOBSIntensityLowDev* (-1)
              - *EnableDoubleMode* (0)
              - *LineIndex* (0)
              - *Qualifier* (90)
              - *SequenceIndex* (0)
              - *IsLineDeactivated* (0)
              - *IsLineChecked* (0)
              - *OutCheckedIntensity* (0)
              - *SuppressionMode* (-1)
              - *IsVisible* (1)
        - **LUT_List**
          - **LUT**
            - *Channel* (1)
            - *LutName* (Green)
        - **DetectorList**
          - *DetectorAutoSelection* (1)
          - *InExternalDetectionMode* (0)
          - **Detector**
            - *Name* (HyD 1)
            - *Type* (HyD)
            - *ScanType* (Internal)
            - *Channel* (1)
            - *ChannelName* (Channel 1)
            - *IsActive* (0)
            - *Gain* (99.9981315396114)
            - *Offset* (-6.6666666666606E-03)
            - *IsSTEDDetector* (1)
            - *IsFlimDetector* (0)
            - *IsHPDDetector* (1)
            - *IsEnabled* (0)
            - *IsHPDOverloaded* (0)
            - *CanDoPhotonCounting* (1)
            - *AcquisitionMode* (0)
            - *AcquisitionModeName* (PhotonIntegration)
            - *CanDoTimeGate* (1)
            - *IsTimeGateActivated* (0)
            - *TimeGatePulseStart* (300)
            - *TimeGateWavelength* (-1)
            - *TimeGatePulseEnd* (6000)
        - **LaserArray**
          - **Laser**
            - *Version* (3)
            - *Qualifier* (90)
            - *QualifierName* (WLL)
            - *LightSourceQualifier* (70)
            - *LightSourceName* (SuperCont)
            - *LaserName* (WLL)
            - *PowerState* (Off)
            - *StedAlignFlag* (1)
            - *CanDoLinearOutputPower* (1)
            - *CanDoPulsing* (1)
            - *CanDoOutputPowerWatt* (1)
            - *HighPowerModeActive* (0)
            - *OutputPowerWatt* (0)
            - *OutputPowerPercentage* (0)
            - *Wavelength* (0)
            - *PulsePickerRatio* (0)
            - *CanDoChangeWavelength* (0)
        - **ROI**
          - **LMSDataContainerHeader**
            - *Version* (2)
            - **Element**
              - *Name* (DCROISet)
              - *Visibility* (2)
              - *CopyOption* (1)
              - *UniqueID* (83457452-b08e-11e4-8e53-bcf685d7650c)
              - **Data**
                - **ROISet**
                  - *ROISetType* (1)
                  - *PossibleChildROITypes* (-1)
                  - *PossibleROITransforms* (65535)
                  - *PossibleROIActions* (65535)
              - **Memory**
                - *Size* (0)
                - *MemoryBlockID* (MemBlock_202)
              - **Children**
        - **CompensationInterpolationPoints**
          - **IntensityCompArray**
        - **OnlineDyeSeparation**
          - *Enabled* (0)
          - *KeepRawImage* (0)
          - *Detectors* (0)
          - *Channels* (0)
          - *Normalize* (0)
          - **OnlineDyeSeparationDetectorList**
          - **OnlineDyeSeparationChannelList**
