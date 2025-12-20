# TextBoxes.AddByRectangle Method

Parent Object: [TextBoxes](../TextBoxes/TextBoxes.md)

## Description

Method that creates a text box whose size is defined by the \input points that define opposing diagonals of the text box.

## Syntax

TextBoxes.**AddByRectangle**( ***CornerOne*** As [Point2d](../Point2d/Point2d.md), ***CornerTwo*** As [Point2d](../Point2d/Point2d.md), ***FormattedText*** As String, [***TextStyle***] As Variant ) As [TextBox](../TextBox/TextBox.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CornerOne | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the first corner of the rectangle. |
| CornerTwo | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the diagonal corner of the rectangle. |
| FormattedText | String | Input String that specifies the text of the text box. This string can contain tags that define internal formatting changes, which override the text style of the text box. See the list of XML text formatting tags under Reference Topics in the Overviews section. |
| TextStyle | Variant | Optional input Variant that specifies which text style to use for the text box. The text style can be specified by providing the name of an existing style or by supplying a TextStyle object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Title Block Definition Create and Insert](../../sample-programs/TitleBlockDefinition_Sample.md) | This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |