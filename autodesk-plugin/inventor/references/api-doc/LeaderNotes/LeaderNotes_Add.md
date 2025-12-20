# LeaderNotes.Add Method

Parent Object: [LeaderNotes](../LeaderNotes/LeaderNotes.md)

## Description

Method that creates a leader note.

## Syntax

LeaderNotes.**Add**( ***LeaderPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***FormattedText*** As String, [***DimensionStyle***] As Variant ) As [LeaderNote](../LeaderNote/LeaderNote.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LeaderPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | ObjectCollection containing a series of Point2d objects representing the leader originating at the note. The last item in the collection (even if it is the only item) can be a GeometryIntent object indicating a geometry to attach the leader to. A GeometryIntent object can be created using the Sheet.CreateGeometryIntent method. The ObjectCollection must contain at least one item, else the method will fail. |
| FormattedText | String | Input String that specifies the text of the general note. This string can contain tags that define internal formatting changes, which override the text style associated with the general note. The formatting is specified using XML tags within the string. By default, all text in the string will be displayed using the text style assigned to the note. You can use the XML tags to override the default style and apply style overrides for all or portions of the text. The formatting overrides are defined using tags. There is an opening tag and closing tag for each formatting override you define. The text between the opening and closing tags is affected by the override. See the list of XML text formatting tags under Reference Topics in the Overviews section. |
| DimensionStyle | Variant | Specifies which dimension style to use for the leader note. The dimension style can be specified by providing the name of an existing style or by supplying a DimensionStyle object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add new leader note](../../sample-programs/LeaderNode_Sample.md) | This sample illustrates creating leader text on a sheet. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |