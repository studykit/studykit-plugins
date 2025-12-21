# GeneralNotes.AddByRectangle Method

Parent Object: [GeneralNotes](../GeneralNotes/GeneralNotes.md)

## Description

Method that creates a general note whose size is defined by the input points that define opposing diagonals of the note.

## Syntax

GeneralNotes.**AddByRectangle**( ***CornerOne*** As [Point2d](../Point2d/Point2d.md), ***CornerTwo*** As [Point2d](../Point2d/Point2d.md), ***FormattedText*** As String, [***TextStyle***] As Variant ) As [GeneralNote](../GeneralNote/GeneralNote.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CornerOne | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the first corner of the rectangle. |
| CornerTwo | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the second corner of the rectangle. |
| FormattedText | String | Input String that specifies the text of the general note. This string can contain tags that define internal formatting changes, which override the text style associated with the general note. The formatting is specified using XML tags within the string. By default, all text in the string will be displayed using the text style assigned to the note. You can use the XML tags to override the default style and apply style overrides for all or portions of the text.  The formatting overrides are defined using tags. There is an opening tag and closing tag for each formatting override you define. The text between the opening and closing tags is affected by the override. See the list of XML text formatting tags under Reference Topics in the Overviews section. |
| TextStyle | Variant | Optional input Variant that specifies which text style to use for the general note. The text style can be specified by providing the name of an existing style or by supplying a TextStyle object. |

## Version

Introduced in version 10
