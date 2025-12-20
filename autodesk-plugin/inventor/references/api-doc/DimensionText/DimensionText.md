# DimensionText Object

## Description

The DimensionText object represents text in a dimension placed on a sheet.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DimensionText/DimensionText_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BackgroundColor](../DimensionText/DimensionText_BackgroundColor.md) | Gets and sets the BackgroundColor associated with the DimensionText. |
| [Color](../DimensionText/DimensionText_Color.md) | Gets and sets the Color Object of the text. |
| [FormattedText](../DimensionText/DimensionText_FormattedText.md) | Gets and sets the formatted text. |
| [HorizontalJustification](../DimensionText/DimensionText_HorizontalJustification.md) | Gets and sets the horizontal justification of the text. |
| [LineSpacing](../DimensionText/DimensionText_LineSpacing.md) | Gets and sets the line spacing of the text. |
| [LineSpacingType](../DimensionText/DimensionText_LineSpacingType.md) | Gets and sets the line spacing method of the text. |
| [Origin](../DimensionText/DimensionText_Origin.md) | Gets and sets the origin position of the text. |
| [Parent](../DimensionText/DimensionText_Parent.md) | Property that returns the parent of the object. |
| [RangeBox](../DimensionText/DimensionText_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [Text](../DimensionText/DimensionText_Text.md) | Property that indicates the string that defines the dimension text. When getting this property, the returned string has all formatting removed and contains the actual text characters displayed in the text. If this property is used to set the text, all format overrides will be removed and the text will revert to the associated text style. Also, the dimension value will always be placed at the beginning of the text. If you want to control the location of the dimension value, use the FormattedText property. The dimension value can be hidden using the HideValue property. |
| [Type](../DimensionText/DimensionText_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseBackgroundColor](../DimensionText/DimensionText_UseBackgroundColor.md) | Gets and sets the UseBackgroundColor associated with the DimensionText. |
| [VerticalJustification](../DimensionText/DimensionText_VerticalJustification.md) | Gets and sets the vertical justification of the text. |
| [WidthScale](../DimensionText/DimensionText_WidthScale.md) | Gets and sets the width scale factor of the text. |

## Accessed From

[AngularGeneralDimension.Text](../AngularGeneralDimension/AngularGeneralDimension_Text.md), [DiameterGeneralDimension.Text](../DiameterGeneralDimension/DiameterGeneralDimension_Text.md), [DrawingDimension.Text](../DrawingDimension/DrawingDimension_Text.md), [GeneralDimension.Text](../GeneralDimension/GeneralDimension_Text.md), [HoleThreadNote.Text](../HoleThreadNote/HoleThreadNote_Text.md), [LinearGeneralDimension.Text](../LinearGeneralDimension/LinearGeneralDimension_Text.md), [OrdinateDimension.Text](../OrdinateDimension/OrdinateDimension_Text.md), [RadiusGeneralDimension.Text](../RadiusGeneralDimension/RadiusGeneralDimension_Text.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Aligning drawing dimensions](../../sample-programs/DrawingDimension_Text_Sample.md) | This sample demonstrates aligning the selected drawing dimensions along a horizontal or vertical axis. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |