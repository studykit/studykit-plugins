# FeatureControlFrameStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

The FeatureControlFrameStyle object represents a feature control frame style in a drawing. The properties and methods listed below are in addition to those supported by the Style object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../FeatureControlFrameStyle/FeatureControlFrameStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../FeatureControlFrameStyle/FeatureControlFrameStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../FeatureControlFrameStyle/FeatureControlFrameStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetAvailableAdditionalSymbols](../FeatureControlFrameStyle/FeatureControlFrameStyle_GetAvailableAdditionalSymbols.md) | Gets the array of FeatureControlFrameAdditionalSymbolsEnum indicating the additional symbols to be made available in the feature control frame creation and edit dialog. |
| [GetReferenceKey](../FeatureControlFrameStyle/FeatureControlFrameStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveToGlobal](../FeatureControlFrameStyle/FeatureControlFrameStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [SetAvailableAdditionalSymbols](../FeatureControlFrameStyle/FeatureControlFrameStyle_SetAvailableAdditionalSymbols.md) | Sets the array of FeatureControlFrameAdditionalSymbolsEnum to specify additional symbols to be made available in the feature control frame creation and edit dialog. |
| [UpdateFromGlobal](../FeatureControlFrameStyle/FeatureControlFrameStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AlignCellsVertically](../FeatureControlFrameStyle/FeatureControlFrameStyle_AlignCellsVertically.md) | Property that gets and sets whether to add spaces to short cells so that pairs of cells align vertically. |
| [AllowTolerance2](../FeatureControlFrameStyle/FeatureControlFrameStyle_AllowTolerance2.md) | Property that gets and sets whether to provide the ability to add a second tolerance in the feature control frame dialog. |
| [AlternateDecimalMarkerType](../FeatureControlFrameStyle/FeatureControlFrameStyle_AlternateDecimalMarkerType.md) | Property that gets and sets the character to use as a decimal marker for alternate units. Valid values are kPeriodDecimalMarker and kCommaDecimalMarker. This property is used only when the AlternateUnitsDisplay property is set to true. |
| [AlternateDisplayUnitType](../FeatureControlFrameStyle/FeatureControlFrameStyle_AlternateDisplayUnitType.md) | Property that gets and sets the arrangement of the alternate units display with respect to the primary units. The primary unit always precedes the alternate unit. This property is used only when the AlternateUnitsDisplay property is set to true. |
| [AlternateLeadingZeroDisplay](../FeatureControlFrameStyle/FeatureControlFrameStyle_AlternateLeadingZeroDisplay.md) | Property that gets and sets whether to display the leading zeroes for alternate units. This property is used only when the AlternateUnitsDisplay property is set to true. |
| [AlternateLinearPrecision](../FeatureControlFrameStyle/FeatureControlFrameStyle_AlternateLinearPrecision.md) | Property that gets and sets the precision for linear alternate units. This property is used only when the AlternateUnitsDisplay property is set to true. |
| [AlternateLinearUnits](../FeatureControlFrameStyle/FeatureControlFrameStyle_AlternateLinearUnits.md) | Property that gets and sets the units of length measure used for alternate units. This property is used only when the AlternateUnitsDisplay property is set to true. |
| [AlternateTrailingZeroDisplay](../FeatureControlFrameStyle/FeatureControlFrameStyle_AlternateTrailingZeroDisplay.md) | Property that gets and sets whether to display the trailing zeroes for alternate units. This property is used only when the AlternateUnitsDisplay property is set to true. |
| [AlternateUnitsDisplay](../FeatureControlFrameStyle/FeatureControlFrameStyle_AlternateUnitsDisplay.md) | Property that gets and sets whether to display alternate units. |
| [AlternateUnitsDisplayType](../FeatureControlFrameStyle/FeatureControlFrameStyle_AlternateUnitsDisplayType.md) | Property that gets and sets the arrangement of the alternate units display with respect to the primary units. The primary unit always precedes the alternate unit. This property is used only when the AlternateUnitsDisplay property is set to true. |
| [Application](../FeatureControlFrameStyle/FeatureControlFrameStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttachLeaderToCorner](../FeatureControlFrameStyle/FeatureControlFrameStyle_AttachLeaderToCorner.md) | Property that gets and sets whether the leader terminates on the corner of the frame or at the midpoint of a vertical leg of the frame. |
| [AvailableGeometricCharacteristics](../FeatureControlFrameStyle/FeatureControlFrameStyle_AvailableGeometricCharacteristics.md) | Property that gets and sets the geometric characteristics to be made available in the feature control frame creation and edit dialog. A combination of enum values can be provided. |
| [AvailableModifiers](../FeatureControlFrameStyle/FeatureControlFrameStyle_AvailableModifiers.md) | Property that gets and sets the material removal modifiers to be made available in the feature control frame creation and edit dialog. A combination of enum values can be provided. |
| [Comments](../FeatureControlFrameStyle/FeatureControlFrameStyle_Comments.md) | Gets and sets comments associated with the style. |
| [DecimalMarkerType](../FeatureControlFrameStyle/FeatureControlFrameStyle_DecimalMarkerType.md) | Property that gets and sets the character to use as a decimal marker for primary units. Valid values are kPeriodDecimalMarker and kCommaDecimalMarker. |
| [DisplayUnitType](../FeatureControlFrameStyle/FeatureControlFrameStyle_DisplayUnitType.md) | Property that gets and sets whether to display units string for primary units. |
| [EnableAuxiliaryFeatureIndicators](../FeatureControlFrameStyle/FeatureControlFrameStyle_EnableAuxiliaryFeatureIndicators.md) | Gets and sets whether the auxiliary feature indicators is enabled or not. |
| [EnableInlineNotes](../FeatureControlFrameStyle/FeatureControlFrameStyle_EnableInlineNotes.md) | Gets and sets whether the inline notes is enabled or not. |
| [InternalName](../FeatureControlFrameStyle/FeatureControlFrameStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../FeatureControlFrameStyle/FeatureControlFrameStyle_InUse.md) | Property that indicates if this style is in use. |
| [LeaderStyle](../FeatureControlFrameStyle/FeatureControlFrameStyle_LeaderStyle.md) | Property that gets and sets the leader style used for a feature control frame symbol. |
| [LeadingZeroDisplay](../FeatureControlFrameStyle/FeatureControlFrameStyle_LeadingZeroDisplay.md) | Property that gets and sets whether to display the leading zeroes for primary units. |
| [LinearUnits](../FeatureControlFrameStyle/FeatureControlFrameStyle_LinearUnits.md) | Property that gets and sets the units of length measure. |
| [MergeDatum](../FeatureControlFrameStyle/FeatureControlFrameStyle_MergeDatum.md) | Property that gets and sets whether to merge datum cells when the data is the same. |
| [MergeSymbol](../FeatureControlFrameStyle/FeatureControlFrameStyle_MergeSymbol.md) | Property that gets and sets whether to merge symbol cells when the data is the same. |
| [MergeTolerance](../FeatureControlFrameStyle/FeatureControlFrameStyle_MergeTolerance.md) | Property that gets and sets whether to merge tolerance cells when the data is the same. |
| [Name](../FeatureControlFrameStyle/FeatureControlFrameStyle_Name.md) | Gets/Sets the name of the Style. |
| [Parent](../FeatureControlFrameStyle/FeatureControlFrameStyle_Parent.md) | Property returning the parent of this object. |
| [ScaleToTextHeight](../FeatureControlFrameStyle/FeatureControlFrameStyle_ScaleToTextHeight.md) | Property that gets and sets whether to define the symbol size by text height. |
| [Size](../FeatureControlFrameStyle/FeatureControlFrameStyle_Size.md) | Property that gets and sets the size of the feature control frame in linear units. This value is used only if the ScaleToTextHeight property is set to False. |
| [StyleLocation](../FeatureControlFrameStyle/FeatureControlFrameStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../FeatureControlFrameStyle/FeatureControlFrameStyle_StyleType.md) | Gets the type of the style. |
| [TextStyle](../FeatureControlFrameStyle/FeatureControlFrameStyle_TextStyle.md) | Property that gets and sets the text style used to format the text in a feature control frame symbol. |
| [TrailingZeroDisplay](../FeatureControlFrameStyle/FeatureControlFrameStyle_TrailingZeroDisplay.md) | Property that gets and sets whether to display the trailing zeroes for primary units. |
| [Type](../FeatureControlFrameStyle/FeatureControlFrameStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpToDate](../FeatureControlFrameStyle/FeatureControlFrameStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |
| [WhiteSpace](../FeatureControlFrameStyle/FeatureControlFrameStyle_WhiteSpace.md) | Property that gets and sets the space before and after text in the tolerance and datum cells. |

## Accessed From

[FeatureControlFrame.Style](../FeatureControlFrame/FeatureControlFrame_Style.md), [FeatureControlFrameStylesEnumerator.Item](../FeatureControlFrameStylesEnumerator/FeatureControlFrameStylesEnumerator_Item.md), [ObjectDefaultsStyle.FeatureControlFrameStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_FeatureControlFrameStyle.md)

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |