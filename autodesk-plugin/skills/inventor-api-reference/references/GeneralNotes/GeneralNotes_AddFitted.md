# GeneralNotes.AddFitted Method

Parent Object: [GeneralNotes](../GeneralNotes/GeneralNotes.md)

## Description

Method that creates a fitted general note positioned at the specified point on the sheet.

## Syntax

GeneralNotes.**AddFitted**( ***PlacementPoint*** As [Point2d](../Point2d/Point2d.md), ***FormattedText*** As String, [***TextStyle***] As Variant ) As [GeneralNote](../GeneralNote/GeneralNote.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PlacementPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the position of the general note on the sheet. The position of this point in relation to the resulting text string is dependent on the vertical and horizontal justification of the note. For example if the vertical justification is the top and horizontal is the left, then the position point defines the upper-left corner of the note. If the vertical justification is the center and the horizontal justification is the center, the position point defines the center of the \note. |
| FormattedText | String | Input String that specifies the text of the general note. This string can contain tags that define internal formatting changes, which override the text style associated with the general note. The formatting is specified using XML tags within the string. By default, all text in the string will be displayed using the text style assigned to the note. You can use the XML tags to override the default style and apply style overrides for all or portions of the text.  The formatting overrides are defined using tags. There is an opening tag and closing tag for each formatting override you define. The text between the opening and closing tags is affected by the override. See the list of XML text formatting tags under Reference Topics in the Overviews section. |
| TextStyle | Variant | Optional input Variant that specifies which text style to use for the general note. The text style can be specified by providing the name of an existing style or by supplying a TextStyle object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add a general note](../../sample-programs/GeneralNote_Sample.md) | This sample illustrates creating text (general note) in a sheet. |
| [Creating Stacked Text](../../sample-programs/GeneralNotes_Sample.md) | This sample demonstrates the creation of stacked text and text with superscript & subscript. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |