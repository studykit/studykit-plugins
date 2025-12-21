# DimensionText.Text Property

Parent Object: [DimensionText](../DimensionText/DimensionText.md)

## Description

Property that indicates the string that defines the dimension text. When getting this property, the returned string has all formatting removed and contains the actual text characters displayed in the text. If this property is used to set the text, all format overrides will be removed and the text will revert to the associated text style. Also, the dimension value will always be placed at the beginning of the text. If you want to control the location of the dimension value, use the FormattedText property. The dimension value can be hidden using the HideValue property.

## Syntax

DimensionText.**Text**() As String

## Property Value

This is a read only property whose value is a String.

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |