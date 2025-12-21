# ModelHoleThreadNotes.CreateDefinition Method

Parent Object: [ModelHoleThreadNotes](../ModelHoleThreadNotes/ModelHoleThreadNotes.md)

## Description

Method that creates a hole or thread note definition. This is a not a hole or thread note but an object that encapsulates all of the information that defines a hole or thread note. You use the methods and properties of this object to define the hole or thread note you want to create and then provide it as input to the Add method.

## Syntax

ModelHoleThreadNotes.**CreateDefinition**( ***Intent*** As [GeometryIntent](../GeometryIntent/GeometryIntent.md), ***AnnotationPlaneDefinition*** As [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md), ***LandingPosition*** As [Point](../Point/Point.md) ) As [ModelHoleThreadNoteDefinition](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Intent | [GeometryIntent](../GeometryIntent/GeometryIntent.md) | Input GeometryIntent object that defines the hole or thread geometry to attach the note to. The intent object must reference geometry associated with a hole or thread, otherwise an error will occur. |
| AnnotationPlaneDefinition | [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md) | Input AnnotationPlaneDefinition object that defines the annotation plane the annotation will be created on. An existing annotation plane can be specified by using the AnnotationPlaneDefinition object associated with the existing annotation plane. |
| LandingPosition | [Point](../Point/Point.md) | Input Point object that specifies the landing position of the note. The point will be projected onto the orientation plane. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |