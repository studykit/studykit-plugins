# TextStyle Object

Derived from: [Style](../Style/Style.md) Object

## Description

The TextStyle object represents a text style in a drawing.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToLocal](../TextStyle/TextStyle_ConvertToLocal.md) | Method that creates a local cached copy of a global style and returns the local style. |
| [Copy](../TextStyle/TextStyle_Copy.md) | Method that creates a new local Style object. The newly created style is returned. |
| [Delete](../TextStyle/TextStyle_Delete.md) | Method that deletes the Style/Layer/UnfoldMethod. |
| [GetReferenceKey](../TextStyle/TextStyle_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SaveToGlobal](../TextStyle/TextStyle_SaveToGlobal.md) | Method that saves this style to the global repository. If a style with the same name is found in the repository, that style is updated. |
| [UpdateFromGlobal](../TextStyle/TextStyle_UpdateFromGlobal.md) | Method that updates this style from the global repository. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TextStyle/TextStyle_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Bold](../TextStyle/TextStyle_Bold.md) | Gets and sets whether the text style has bold formatting or not. True if the text style has bold formatting. |
| [Color](../TextStyle/TextStyle_Color.md) | Gets and sets the current color of the text. |
| [Comments](../TextStyle/TextStyle_Comments.md) | Gets and sets comments associated with the style. |
| [Font](../TextStyle/TextStyle_Font.md) | Gets and sets the font used for the text style. |
| [FontSize](../TextStyle/TextStyle_FontSize.md) | Gets and sets the size of the font. The size is specified in centimeters. |
| [HorizontalJustification](../TextStyle/TextStyle_HorizontalJustification.md) | Gets and sets the horizontal justification of the text style. |
| [InternalName](../TextStyle/TextStyle_InternalName.md) | Property that returns the internal name of the style. The name is the internal English name of the standard style. This name will remain constant and is not affected by locale. This name is never displayed to the user. Note that this name is not guaranteed to be unique. |
| [InUse](../TextStyle/TextStyle_InUse.md) | Property that indicates if this style is in use. |
| [Italic](../TextStyle/TextStyle_Italic.md) | Gets and sets whether the text style has italic formatting or not. True if the text style has italic formatting. |
| [LineSpacing](../TextStyle/TextStyle_LineSpacing.md) | Gets and sets the line spacing of the text style. |
| [LineSpacingType](../TextStyle/TextStyle_LineSpacingType.md) | Gets and sets the method used to define the line spacing. |
| [Name](../TextStyle/TextStyle_Name.md) | Gets/Sets the name of the Style. |
| [Parent](../TextStyle/TextStyle_Parent.md) | Property returning the parent of this object. |
| [Rotation](../TextStyle/TextStyle_Rotation.md) | Gets and sets the rotation of the text style. The units used to define the rotation angle are radians. Currently text rotation is limited to 90 degree increments so valid values for this property are 0, pi/2, pi, and 1.5pi. |
| [StyleLocation](../TextStyle/TextStyle_StyleLocation.md) | Property that returns the location of this style, i.e. local to the document, cached locally in the document, exists in the library. Styles that exist in the library cannot be edited. |
| [StyleType](../TextStyle/TextStyle_StyleType.md) | Gets the type of the style. |
| [Type](../TextStyle/TextStyle_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Underline](../TextStyle/TextStyle_Underline.md) | Gets and sets whether the text style has underline formatting or not. True if the text style has underline formatting. |
| [UpToDate](../TextStyle/TextStyle_UpToDate.md) | Property that gets the up-to-date status of the style against the global repository. |
| [VerticalJustification](../TextStyle/TextStyle_VerticalJustification.md) | Gets and sets the vertical justification of the text style. |
| [WidthScale](../TextStyle/TextStyle_WidthScale.md) | Gets and sets the width scale factor for the text style. This is also referred to as the 'stretch factor'. A value of 1.0 will display the text as designed; a value of 0.5 will decrease the width of the text by 50%. |

## Accessed From

[BalloonStyle.TextStyle](../BalloonStyle/BalloonStyle_TextStyle.md), [CustomTable.ColumnHeaderTextStyle](../CustomTable/CustomTable_ColumnHeaderTextStyle.md), [CustomTable.DataTextStyle](../CustomTable/CustomTable_DataTextStyle.md), [CustomTable.TitleTextStyle](../CustomTable/CustomTable_TitleTextStyle.md), [DimensionStyle.TextStyle](../DimensionStyle/DimensionStyle_TextStyle.md), [DimensionStyle.ToleranceTextStyle](../DimensionStyle/DimensionStyle_ToleranceTextStyle.md), [DrawingViewLabel.TextStyle](../DrawingViewLabel/DrawingViewLabel_TextStyle.md), [EdgeSymbolStyle.TextStyle](../EdgeSymbolStyle/EdgeSymbolStyle_TextStyle.md), [FeatureControlFrameStyle.TextStyle](../FeatureControlFrameStyle/FeatureControlFrameStyle_TextStyle.md), [GeneralNote.TextStyle](../GeneralNote/GeneralNote_TextStyle.md), [HoleTable.ColumnHeaderTextStyle](../HoleTable/HoleTable_ColumnHeaderTextStyle.md), [HoleTable.DataTextStyle](../HoleTable/HoleTable_DataTextStyle.md), [HoleTable.TitleTextStyle](../HoleTable/HoleTable_TitleTextStyle.md), [HoleTableStyle.ColumnHeaderTextStyle](../HoleTableStyle/HoleTableStyle_ColumnHeaderTextStyle.md), [HoleTableStyle.DataTextStyle](../HoleTableStyle/HoleTableStyle_DataTextStyle.md), [HoleTableStyle.TitleTextStyle](../HoleTableStyle/HoleTableStyle_TitleTextStyle.md), [ObjectDefaultsStyle.BorderTextStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_BorderTextStyle.md), [ObjectDefaultsStyle.GeneralNoteStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_GeneralNoteStyle.md), [ObjectDefaultsStyle.SketchedSymbolTextStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_SketchedSymbolTextStyle.md), [ObjectDefaultsStyle.SketchTextStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_SketchTextStyle.md), [ObjectDefaultsStyle.TitleBlockTextStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_TitleBlockTextStyle.md), [ObjectDefaultsStyle.ViewLabelStyle](../ObjectDefaultsStyle/ObjectDefaultsStyle_ViewLabelStyle.md), [PartsList.ColumnHeaderTextStyle](../PartsList/PartsList_ColumnHeaderTextStyle.md), [PartsList.DataTextStyle](../PartsList/PartsList_DataTextStyle.md), [PartsList.TitleTextStyle](../PartsList/PartsList_TitleTextStyle.md), [PartsListStyle.ColumnHeaderTextStyle](../PartsListStyle/PartsListStyle_ColumnHeaderTextStyle.md), [PartsListStyle.DataTextStyle](../PartsListStyle/PartsListStyle_DataTextStyle.md), [PartsListStyle.TitleTextStyle](../PartsListStyle/PartsListStyle_TitleTextStyle.md), [RevisionTable.ColumnHeaderTextStyle](../RevisionTable/RevisionTable_ColumnHeaderTextStyle.md), [RevisionTable.DataTextStyle](../RevisionTable/RevisionTable_DataTextStyle.md), [RevisionTable.TitleTextStyle](../RevisionTable/RevisionTable_TitleTextStyle.md), [RevisionTableStyle.ColumnHeaderTextStyle](../RevisionTableStyle/RevisionTableStyle_ColumnHeaderTextStyle.md), [RevisionTableStyle.DataTextStyle](../RevisionTableStyle/RevisionTableStyle_DataTextStyle.md), [RevisionTableStyle.RevisionTagTextStyle](../RevisionTableStyle/RevisionTableStyle_RevisionTagTextStyle.md), [RevisionTableStyle.TitleTextStyle](../RevisionTableStyle/RevisionTableStyle_TitleTextStyle.md), [SurfaceTextureStyle.TextStyle](../SurfaceTextureStyle/SurfaceTextureStyle_TextStyle.md), [TableFormat.TextStyle](../TableFormat/TableFormat_TextStyle.md), [TableStyle.ColumnHeaderTextStyle](../TableStyle/TableStyle_ColumnHeaderTextStyle.md), [TableStyle.DataTextStyle](../TableStyle/TableStyle_DataTextStyle.md), [TableStyle.TitleTextStyle](../TableStyle/TableStyle_TitleTextStyle.md), [TextBox.Style](../TextBox/TextBox_Style.md), [TextBoxProxy.Style](../TextBoxProxy/TextBoxProxy_Style.md), [TextStyles.Item](TextStyles_Item.md), [TextStylesEnumerator.Item](../TextStylesEnumerator/TextStylesEnumerator_Item.md), [TransitionSymbolStyle.TextStyle](../TransitionSymbolStyle/TransitionSymbolStyle_TextStyle.md), [WeldSymbolStyle.TextStyle](../WeldSymbolStyle/WeldSymbolStyle_TextStyle.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch Text Add](../../sample-programs/TextBoxes_Sample.md) | This sample illustrates creating text in a sketch. |

## Version

Introduced in version 5.3
