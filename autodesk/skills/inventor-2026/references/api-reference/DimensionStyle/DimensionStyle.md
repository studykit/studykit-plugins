# DimensionStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

The DimensionStyle object represents a dimension style in a drawing.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../DimensionStyle/DimensionStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../DimensionStyle/DimensionStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../DimensionStyle/DimensionStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetCustomLineType](../DimensionStyle/DimensionStyle_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetHoleThreadNoteOptionValue](../DimensionStyle/DimensionStyle_GetHoleThreadNoteOptionValue.md) | Gets the option value for hole thread notes. |
| [GetReferenceKey](../DimensionStyle/DimensionStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveToGlobal](../DimensionStyle/DimensionStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [SetCustomLineType](../DimensionStyle/DimensionStyle_SetCustomLineType.md) | Method that sets a custom line type to the style from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |
| [SetHoleThreadNoteOptionValue](../DimensionStyle/DimensionStyle_SetHoleThreadNoteOptionValue.md) | Sets the option value for hole thread notes. |
| [UpdateFromGlobal](../DimensionStyle/DimensionStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AlignedDimensionTextOrientation](../DimensionStyle/DimensionStyle_AlignedDimensionTextOrientation.md) | Gets and sets the orientation of the text in an aligned dimension. |
| [AlternateDecimalMarkerType](../DimensionStyle/DimensionStyle_AlternateDecimalMarkerType.md) | Gets and sets the character to use as a decimal marker for alternate dimensions. |
| [AlternateDisplayFormat](../DimensionStyle/DimensionStyle_AlternateDisplayFormat.md) | Gets and sets the alternate units display format for all non-angular dimensions. |
| [AlternateDisplayUnitType](../DimensionStyle/DimensionStyle_AlternateDisplayUnitType.md) | Gets and sets whether to display units for alternate dimensions in the drawing. |
| [AlternateFractionalTextScale](../DimensionStyle/DimensionStyle_AlternateFractionalTextScale.md) | Gets and sets the size of the stacked text relative to the default text size when using alternate units. The valid range of values is 0.25 to 1.25. |
| [AlternateIncludedZeroDisplay](../DimensionStyle/DimensionStyle_AlternateIncludedZeroDisplay.md) | Gets and sets whether to display the included zeroes for alternate dimensions in the drawing. |
| [AlternateLeadingZeroDisplay](../DimensionStyle/DimensionStyle_AlternateLeadingZeroDisplay.md) | Gets and sets whether to display the leading zeroes for alternate dimensions in the drawing. |
| [AlternateLinearPrecision](../DimensionStyle/DimensionStyle_AlternateLinearPrecision.md) | Gets and sets the precision for linear alternate dimensions in the drawing. |
| [AlternateLinearUnits](../DimensionStyle/DimensionStyle_AlternateLinearUnits.md) | Gets and sets the units of length measure used for alternate dimensions in the drawing. |
| [AlternateTrailingZeroDisplay](../DimensionStyle/DimensionStyle_AlternateTrailingZeroDisplay.md) | Gets and sets whether to display the trailing zeroes for alternate dimensions in the drawing. |
| [AngularArrowsInside](../DimensionStyle/DimensionStyle_AngularArrowsInside.md) | Gets and sets inside or outside placement of arrows for Angular dimensions. |
| [AngularFormatIsDecimalDegrees](../DimensionStyle/DimensionStyle_AngularFormatIsDecimalDegrees.md) | Gets and sets whether to display angular dimension values as decimal degrees or degrees-minutes-seconds. |
| [AngularHideExtensionLineOne](../DimensionStyle/DimensionStyle_AngularHideExtensionLineOne.md) | Gets and sets if the first extension line of an angular dimension is hidden. |
| [AngularHideExtensionLineTwo](../DimensionStyle/DimensionStyle_AngularHideExtensionLineTwo.md) | Gets and sets if the second extension line of an angular dimension is hidden. |
| [AngularLeadingZeroDisplay](../DimensionStyle/DimensionStyle_AngularLeadingZeroDisplay.md) | Gets and sets whether to display the leading zeroes for angular dimensions in the drawing. |
| [AngularPrecision](../DimensionStyle/DimensionStyle_AngularPrecision.md) | Gets and sets the precision for angular dimensions in the drawing. |
| [AngularTextModifier](../DimensionStyle/DimensionStyle_AngularTextModifier.md) | Gets and sets the optional modifier that controls the controls the position of text in an angular dimension. |
| [AngularTextOrientation](../DimensionStyle/DimensionStyle_AngularTextOrientation.md) | Gets and sets the orientation of angular dimension text. |
| [AngularTrailingZeroDisplay](../DimensionStyle/DimensionStyle_AngularTrailingZeroDisplay.md) | Gets and sets whether to display the trailing zeroes for angular dimensions in the drawing. |
| [AngularUseQuadrant](../DimensionStyle/DimensionStyle_AngularUseQuadrant.md) | Gets and sets whether to use a quadrant or ignore the quadrant angular dimension text. |
| [Application](../DimensionStyle/DimensionStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ArcLengthDimensionSymbolAbove](../DimensionStyle/DimensionStyle_ArcLengthDimensionSymbolAbove.md) | Gets and sets whether the arc length dimension symbol is above the arc length dimension value or before it. |
| [ArrowheadHeight](../DimensionStyle/DimensionStyle_ArrowheadHeight.md) | Gets and sets the height of the arrowhead relative to the associated line. |
| [ArrowheadSize](../DimensionStyle/DimensionStyle_ArrowheadSize.md) | Gets and sets the size of the arrowhead. |
| [ArrowheadType](../DimensionStyle/DimensionStyle_ArrowheadType.md) | Gets and sets the arrowhead style to use. |
| [ArrowheadTypeForChainDimensions](../DimensionStyle/DimensionStyle_ArrowheadTypeForChainDimensions.md) | Gets and sets the internal arrowhead styles to use for chain dimensions. |
| [BasicDimensionPrefixSuffixInside](../DimensionStyle/DimensionStyle_BasicDimensionPrefixSuffixInside.md) | Gets and sets whether the prefix and suffix are inside or outside the basic dimension box. |
| [BendNoteDualFormat](../DimensionStyle/DimensionStyle_BendNoteDualFormat.md) | Gets and sets the arrangement of the alternate dimension display for bend notes. |
| [ChamferNoteDualFormat](../DimensionStyle/DimensionStyle_ChamferNoteDualFormat.md) | Gets and sets the arrangement of the alternate dimension display for chamfer notes. |
| [Color](../DimensionStyle/DimensionStyle_Color.md) | Gets and sets the color for the style. |
| [Comments](../DimensionStyle/DimensionStyle_Comments.md) | Gets and sets comments associated with the style. |
| [DecimalMarkerType](../DimensionStyle/DimensionStyle_DecimalMarkerType.md) | Gets and sets the character to use as a decimal marker for dimensions. |
| [DiameterArrowsInside](../DimensionStyle/DimensionStyle_DiameterArrowsInside.md) | Gets and sets inside or outside placement of arrows for diameter dimensions. |
| [DiameterDualDimensionLine](../DimensionStyle/DimensionStyle_DiameterDualDimensionLine.md) | Gets and sets if single or dual diameter dimension lines should be displayed. |
| [DiameterExternalTextOrientation](../DimensionStyle/DimensionStyle_DiameterExternalTextOrientation.md) | Gets and sets the orientation of text in a diameter dimension when the text is external using a leader line. |
| [DiameterInternalTextOrientation](../DimensionStyle/DimensionStyle_DiameterInternalTextOrientation.md) | Gets and sets the orientation of text in a diameter dimension when the text is within a dimension line. |
| [DiameterLeaderFromCenter](../DimensionStyle/DimensionStyle_DiameterLeaderFromCenter.md) | Gets and sets if the leader line of a diameter dimension extends to the center or not. |
| [DiameterMultiLineTextOrientation](../DimensionStyle/DimensionStyle_DiameterMultiLineTextOrientation.md) | Read-write property that gets and sets the position of multiple lines of text relative to the landing line in a diameter dimension. Valid values are kFirstLineCenteredOnLandingLine, kAllAboveLandingLine, kAllAboveLandingLineWithUnderline, kFirstLineAboveLandingLine, and kJISAlignment. |
| [DiameterShowDiameterSymbol](../DimensionStyle/DimensionStyle_DiameterShowDiameterSymbol.md) | Gets and sets if the diameter symbol should be shown in a diameter dimension. |
| [DimensionDualFormat](../DimensionStyle/DimensionStyle_DimensionDualFormat.md) | Read-write property that gets and sets the arrangement of the alternate dimension display for dimensions. |
| [DisplayFormat](../DimensionStyle/DimensionStyle_DisplayFormat.md) | Gets and sets the display format for all non-angular dimensions. |
| [DisplayUnitType](../DimensionStyle/DimensionStyle_DisplayUnitType.md) | Gets and sets whether to display units for dimensions in the drawing. |
| [ExtendBeyondTicks](../DimensionStyle/DimensionStyle_ExtendBeyondTicks.md) | Gets and sets the distance extend the dimension line past the extension line in centimeters when the arrowheads is specified as oblique or no marks. |
| [Extension](../DimensionStyle/DimensionStyle_Extension.md) | Gets and sets the distance the extension line is drawn past the dimension line. |
| [ExtensionLine](../DimensionStyle/DimensionStyle_ExtensionLine.md) | Gets and sets the length of the extension line in centimeters. |
| [FractionalTextScale](../DimensionStyle/DimensionStyle_FractionalTextScale.md) | Gets and sets the size of the stacked text relative to the default text size. The valid range of values is 0.25 to 1.25. |
| [Gap](../DimensionStyle/DimensionStyle_Gap.md) | Gets and sets the distance between the dimension text and the dimension lines. |
| [HoleNoteDualFormat](../DimensionStyle/DimensionStyle_HoleNoteDualFormat.md) | Gets and sets the arrangement of the alternate dimension display for hole notes. |
| [HoleThreadTypeList](../DimensionStyle/DimensionStyle_HoleThreadTypeList.md) | Returns the hole and thread type list. |
| [HorizontalDimensionTextOrientation](../DimensionStyle/DimensionStyle_HorizontalDimensionTextOrientation.md) | Read-write property that gets and sets the orientation of the text in a horizontal dimension. Valid values are kParallelDimensionText and kInlineHorizontalText. |
| [IncludedZeroDisplay](../DimensionStyle/DimensionStyle_IncludedZeroDisplay.md) | Gets and sets whether to display the included zeroes for dimensions in the drawing. |
| [InternalName](../DimensionStyle/DimensionStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../DimensionStyle/DimensionStyle_InUse.md) | Property that indicates if this style is in use. |
| [LeaderStyle](../DimensionStyle/DimensionStyle_LeaderStyle.md) | Property that gets and sets the leader style used for the dimension style. |
| [LeadingZeroDisplay](../DimensionStyle/DimensionStyle_LeadingZeroDisplay.md) | Gets and sets whether to display the leading zeroes for dimensions in the drawing. |
| [LinearArrowsInside](../DimensionStyle/DimensionStyle_LinearArrowsInside.md) | Gets and sets inside or outside placement of arrows for linear dimensions. |
| [LinearHideExtensionLineOne](../DimensionStyle/DimensionStyle_LinearHideExtensionLineOne.md) | Gets and sets if the first extension line of a linear dimension is hidden. |
| [LinearHideExtensionLineTwo](../DimensionStyle/DimensionStyle_LinearHideExtensionLineTwo.md) | Gets and sets if the second extension line of a linear dimension is hidden. |
| [LinearMultiLineTextOrientation](../DimensionStyle/DimensionStyle_LinearMultiLineTextOrientation.md) | Read-write property that gets and sets the position of multiple lines of text relative to the landing line in a linear dimension. Valid values are kAllAboveLandingLine and kFirstLineAboveLandingLine. |
| [LinearPrecision](../DimensionStyle/DimensionStyle_LinearPrecision.md) | Gets and sets the precision value for linear dimensions in the drawing. |
| [LinearUnits](../DimensionStyle/DimensionStyle_LinearUnits.md) | Gets and sets the units of length measure used for dimensions in the drawing. |
| [LineType](../DimensionStyle/DimensionStyle_LineType.md) | Gets and sets the line type override for the style. |
| [LineWeight](../DimensionStyle/DimensionStyle_LineWeight.md) | Gets and sets the line weight override for the style. |
| [Name](../DimensionStyle/DimensionStyle_Name.md) | Gets/Sets the name of the Style. |
| [OrdinateAlignment](../DimensionStyle/DimensionStyle_OrdinateAlignment.md) | Gets and sets the type of alignment to use for ordinate dimensions. |
| [OrdinateDimensionOriginArrowheadType](../DimensionStyle/DimensionStyle_OrdinateDimensionOriginArrowheadType.md) | Gets and sets the arrowhead type for the origin member of ordinate dimension sets. |
| [OrdinateHideOriginIndicator](../DimensionStyle/DimensionStyle_OrdinateHideOriginIndicator.md) | Gets and sets if the origin indicator is to be hidden or not. |
| [OrdinateJoggingAllowed](../DimensionStyle/DimensionStyle_OrdinateJoggingAllowed.md) | Gets and sets if jogged leaders for ordinate dimensions is allowed or not. |
| [OrdinatePositiveBothDirections](../DimensionStyle/DimensionStyle_OrdinatePositiveBothDirections.md) | Gets and sets if positive values should be shown in both directions or not for an ordinate dimension. |
| [OrdinateShowDirection](../DimensionStyle/DimensionStyle_OrdinateShowDirection.md) | Gets and sets if the direction arrow should be shown or not for ordinate dimensions. |
| [OrdinateUseOriginIndicator](../DimensionStyle/DimensionStyle_OrdinateUseOriginIndicator.md) | Gets and sets if the origin indicator is to be used or not. |
| [OriginOffset](../DimensionStyle/DimensionStyle_OriginOffset.md) | Gets and sets the distance from an edge or point to the endpoint of the extension line. |
| [Parent](../DimensionStyle/DimensionStyle_Parent.md) | Property returning the parent of this object. |
| [PartOffset](../DimensionStyle/DimensionStyle_PartOffset.md) | Gets and sets the distance from the referenced part edge to a parallel dimension line. |
| [Prefix](../DimensionStyle/DimensionStyle_Prefix.md) | Gets and sets the dimension prefix. |
| [PrefixAndSuffixOrder](../DimensionStyle/DimensionStyle_PrefixAndSuffixOrder.md) | Gets and sets the location of prefix and suffix. |
| [PunchNoteDualFormat](../DimensionStyle/DimensionStyle_PunchNoteDualFormat.md) | Gets and sets the arrangement of the alternate dimension display for punch notes. |
| [RadialArrowsInside](../DimensionStyle/DimensionStyle_RadialArrowsInside.md) | Gets and sets inside or outside placement of arrows for radial dimensions. |
| [RadialJoggedLeader](../DimensionStyle/DimensionStyle_RadialJoggedLeader.md) | Gets and sets if the leader line of a radial dimension is jogged or not. |
| [RadialLeaderFromCenter](../DimensionStyle/DimensionStyle_RadialLeaderFromCenter.md) | Gets and sets if the leader line of a radial dimension extends from the center or not. |
| [RadialMultiLineTextOrientation](../DimensionStyle/DimensionStyle_RadialMultiLineTextOrientation.md) | Gets and sets the position of multiple lines of text relative to the landing line in a radial dimension. |
| [RadialTextOrientation](../DimensionStyle/DimensionStyle_RadialTextOrientation.md) | Gets and sets the orientation of text in a radial dimension. |
| [ShowBreakSymbol](../DimensionStyle/DimensionStyle_ShowBreakSymbol.md) | Gets and sets whether to display break symbols for dimensions on a broken view. |
| [ShowDimensionLine](../DimensionStyle/DimensionStyle_ShowDimensionLine.md) | Gets and sets whether to display the dimension line when arrowheads are outside the dimension extension lines. |
| [Spacing](../DimensionStyle/DimensionStyle_Spacing.md) | Gets and sets the distance between the parallel dimension lines. |
| [StyleLocation](../DimensionStyle/DimensionStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../DimensionStyle/DimensionStyle_StyleType.md) | Gets the type of the style. |
| [Suffix](../DimensionStyle/DimensionStyle_Suffix.md) | Gets and sets the dimension suffix. |
| [TextStyle](../DimensionStyle/DimensionStyle_TextStyle.md) | Gets and sets the text style used for the dimension style. |
| [Tolerance](../DimensionStyle/DimensionStyle_Tolerance.md) | Property that returns the Tolerance object. The Tolerance object contains methods and properties to query and modify tolerance types and values. |
| [ToleranceAlternateIncludedZeroDisplay](../DimensionStyle/DimensionStyle_ToleranceAlternateIncludedZeroDisplay.md) | Gets and sets whether to display the included zeroes for tolerances in alternate units. |
| [ToleranceAlternateLeadingZeroDisplay](../DimensionStyle/DimensionStyle_ToleranceAlternateLeadingZeroDisplay.md) | Gets and sets whether to display the leading zeroes for tolerances in alternate units. |
| [ToleranceAlternateTrailingZeroDisplay](../DimensionStyle/DimensionStyle_ToleranceAlternateTrailingZeroDisplay.md) | Gets and sets whether to display the trailing zeroes for tolerances in alternate units. |
| [ToleranceAlternateUnitPrecision](../DimensionStyle/DimensionStyle_ToleranceAlternateUnitPrecision.md) | Gets and sets the number of decimal places visible to the right of the decimal marker in tolerance text for alternate dimensions. |
| [ToleranceAngularPrecision](../DimensionStyle/DimensionStyle_ToleranceAngularPrecision.md) | Gets and sets the precision of the tolerance text for angular dimensions. |
| [ToleranceFontSize](../DimensionStyle/DimensionStyle_ToleranceFontSize.md) | Gets and sets the size of the font used for tolerances. |
| [ToleranceIncludedZeroDisplay](../DimensionStyle/DimensionStyle_ToleranceIncludedZeroDisplay.md) | Gets and sets whether to display the included zeroes for tolerances. |
| [ToleranceJustification](../DimensionStyle/DimensionStyle_ToleranceJustification.md) | Gets and sets the vertical justification of dimension tolerance text. |
| [ToleranceLeadingZeroDisplay](../DimensionStyle/DimensionStyle_ToleranceLeadingZeroDisplay.md) | Gets and sets whether to display the leading zeroes for tolerances. |
| [ToleranceLinearPrecision](../DimensionStyle/DimensionStyle_ToleranceLinearPrecision.md) | Gets and sets the number of decimal places visible to the right of the decimal marker in tolerance text for linear dimensions. |
| [ToleranceShowMinuteSecond](../DimensionStyle/DimensionStyle_ToleranceShowMinuteSecond.md) | Gets and sets whether to show angles using fractional degrees or minutes and seconds. |
| [ToleranceTextStyle](../DimensionStyle/DimensionStyle_ToleranceTextStyle.md) | Gets and sets the text style used for tolerance. |
| [ToleranceTrailingZeroDisplay](../DimensionStyle/DimensionStyle_ToleranceTrailingZeroDisplay.md) | Gets and sets whether to display the trailing zeroes for tolerances. |
| [ToleranceZeroToleranceDisplay](../DimensionStyle/DimensionStyle_ToleranceZeroToleranceDisplay.md) | Gets and sets how to display zero tolerances. |
| [TrailingZeroDisplay](../DimensionStyle/DimensionStyle_TrailingZeroDisplay.md) | Gets and sets whether to display the trailing zeroes for dimensions in the drawing. |
| [Type](../DimensionStyle/DimensionStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../DimensionStyle/DimensionStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |
| [UseCapitalXForEquallySpacedFeatures](../DimensionStyle/DimensionStyle_UseCapitalXForEquallySpacedFeatures.md) | Gets and sets whether to use capital X for equally spaced features or not. |
| [VerticalDimensionTextOrientation](../DimensionStyle/DimensionStyle_VerticalDimensionTextOrientation.md) | Gets and sets the orientation of the text in a vertical dimension. |

## Accessed From

[AngularGeneralDimension.Style](../AngularGeneralDimension/AngularGeneralDimension_Style.md), [BaselineDimensionSet.Style](../BaselineDimensionSet/BaselineDimensionSet_Style.md), [BendNote.DimensionStyle](../BendNote/BendNote_DimensionStyle.md), [ChainDimensionSet.Style](../ChainDimensionSet/ChainDimensionSet_Style.md), [ChamferNote.DimensionStyle](../ChamferNote/ChamferNote_DimensionStyle.md), [DiameterGeneralDimension.Style](../DiameterGeneralDimension/DiameterGeneralDimension_Style.md), [DimensionStylesEnumerator.Item](../DimensionStylesEnumerator/DimensionStylesEnumerator_Item.md), [GeneralDimension.Style](../GeneralDimension/GeneralDimension_Style.md), [HoleTag.DimensionStyle](../HoleTag/HoleTag_DimensionStyle.md), [HoleThreadNote.Style](../HoleThreadNote/HoleThreadNote_Style.md), [LeaderNote.DimensionStyle](../LeaderNote/LeaderNote_DimensionStyle.md), [LinearGeneralDimension.Style](../LinearGeneralDimension/LinearGeneralDimension_Style.md), [ObjectDefaultsStyle.AngularDimensionStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_AngularDimensionStyle.md), [ObjectDefaultsStyle.BaselineDimensionStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_BaselineDimensionStyle.md), [ObjectDefaultsStyle.BendNoteStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_BendNoteStyle.md), [ObjectDefaultsStyle.BendTagStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_BendTagStyle.md), [ObjectDefaultsStyle.ChainDimensionStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_ChainDimensionStyle.md), [ObjectDefaultsStyle.ChamferNoteStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_ChamferNoteStyle.md), [ObjectDefaultsStyle.DiameterDimensionStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_DiameterDimensionStyle.md), [ObjectDefaultsStyle.HoleNoteStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_HoleNoteStyle.md), [ObjectDefaultsStyle.HoleTagStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_HoleTagStyle.md), [ObjectDefaultsStyle.LeaderTextStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_LeaderTextStyle.md), [ObjectDefaultsStyle.LinearDimensionStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_LinearDimensionStyle.md), [ObjectDefaultsStyle.OrdinateDimensionStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_OrdinateDimensionStyle.md), [ObjectDefaultsStyle.OrdinateSetDimensionStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_OrdinateSetDimensionStyle.md), [ObjectDefaultsStyle.PunchNoteStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_PunchNoteStyle.md), [ObjectDefaultsStyle.RadialDimensionStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_RadialDimensionStyle.md), [ObjectDefaultsStyle.ThreadNoteStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_ThreadNoteStyle.md), [OrdinateDimension.Style](../OrdinateDimension/OrdinateDimension_Style.md), [OrdinateDimensionSet.Style](../OrdinateDimensionSet/OrdinateDimensionSet_Style.md), [PunchNote.DimensionStyle](../PunchNote/PunchNote_DimensionStyle.md), [RadiusGeneralDimension.Style](../RadiusGeneralDimension/RadiusGeneralDimension_Style.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Dimensions - edit](../../sample-programs/DrawingDimension_Sample.md) | This sample demonstrates the editing of sheet dimensions and the associated dimension style. |

## Version

Introduced in version 9
