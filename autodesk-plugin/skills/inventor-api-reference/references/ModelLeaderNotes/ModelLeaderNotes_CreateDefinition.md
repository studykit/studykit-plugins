# ModelLeaderNotes.CreateDefinition Method

Parent Object: [ModelLeaderNotes](../ModelLeaderNotes/ModelLeaderNotes.md)

## Description

Method that creates a leader note definition. This is a not a leader note but an object that encapsulates all of the information that defines a leader note. You use the methods and properties of this object to define the leader note you want to create and then provide it as input to the Add method.

## Syntax

ModelLeaderNotes.**CreateDefinition**( ***LeaderPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***FormattedText*** As String, ***AnnotationPlaneDefinition*** As [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md) ) As [ModelLeaderNoteDefinition](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LeaderPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | ObjectCollection containing a series of Point objects representing the leader originating at the note. The last item in the collection (even if it is the only item) can be a GeometryIntent object indicating the geometry to attach the leader to. The ObjectCollection must contain at least one item, else the method will fail. The points are projected onto the orientation plane. |
| FormattedText | String | Input String that specifies the text of the note. This string can contain tags that define internal formatting changes, which override the text style associated with the general note. The formatting is specified using XML tags within the string. By default, all text in the string will be displayed using the text style assigned to the note. You can use the XML tags to override the default style and apply style overrides for all or portions of the text. The formatting overrides are defined using tags. There is an opening tag and closing tag for each formatting override you define. The text between the opening and closing tags is affected by the override. See the list of XML text formatting tags under Reference Topics in the Overviews section. |
| AnnotationPlaneDefinition | [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md) | Input AnnotationPlaneDefinition object that defines the annotation plane the annotation will be created on. An existing annotation plane can be specified by using the AnnotationPlaneDefinition object associated with the existing annotation plane. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |