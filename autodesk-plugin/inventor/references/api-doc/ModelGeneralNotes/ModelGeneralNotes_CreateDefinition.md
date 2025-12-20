# ModelGeneralNotes.CreateDefinition Method

Parent Object: [ModelGeneralNotes](../ModelGeneralNotes/ModelGeneralNotes.md)

## Description

Method that creates a general note definition. This is a not a general note but an object that encapsulates all of the information that defines a general note.

## Syntax

ModelGeneralNotes.**CreateDefinition**( ***FormattedText*** As String, ***OnScreen*** As Boolean, [***ScreenQuadrant***] As Variant, [***AnnotationPlaneDefinition***] As Variant ) As [ModelGeneralNoteDefinition](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FormattedText | String | Input String that specifies the text of the note. This string can contain tags that define internal formatting changes, which override the text style associated with the general note. The formatting is specified using XML tags within the string. By default, all text in the string will be displayed using the text style assigned to the note. You can use the XML tags to override the default style and apply style overrides for all or portions of the text. The formatting overrides are defined using tags. There is an opening tag and closing tag for each formatting override you define. The text between the opening and closing tags is affected by the override. See the list of XML text formatting tags under Reference Topics in the Overviews section. |
| OnScreen | Boolean | Input Boolean value that specifies whether the general note is on screen or not. |
| ScreenQuadrant | Variant | Optional input ScreenQuadrantEnum value that specifies the location of the general note on screen. This is ignored if the OnScreen is specified as False. This defaults to kLowerLeftQuadrant if not specified. |
| AnnotationPlaneDefinition | Variant | Optional input AnnotationPlaneDefinition object that defines the annotation plane the general note will be created on. An existing annotation plane can be specified by using the AnnotationPlaneDefinition object associated with the existing annotation plane. If the OnScreen is specified as True then this argument is ignored, otherwise this is required.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |