# ModelGeneralNoteDefinition.SetToModelSpaceDisplay Method

Parent Object: [ModelGeneralNoteDefinition](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition.md)

## Description

Sets the general note to be displayed in model space. This will set the OnScreen to be False.

## Syntax

ModelGeneralNoteDefinition.**SetToModelSpaceDisplay**( ***AnnotationPlaneDefinition*** As [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md), ***Intent*** As Variant, [***Position***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AnnotationPlaneDefinition | [AnnotationPlaneDefinition](../AnnotationPlaneDefinition/AnnotationPlaneDefinition.md) | Input AnnotationPlaneDefinition object that defines the annotation plane the general note will be on. An existing annotation plane can be specified by using the AnnotationPlaneDefinition object associated with the existing annotation plane. |
| Intent | Variant | Input GeometryIntent that specifies the geometry the general note attaches to, or Point to specify the position for the general note. When input a Point and if the Point is not on the orientation plane, it will be projected onto the orientation plane. |
| Position | Variant | This reserved for future use. |

## Version

Introduced in version 2018
