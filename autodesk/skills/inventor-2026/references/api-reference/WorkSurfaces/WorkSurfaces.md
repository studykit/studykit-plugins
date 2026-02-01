# WorkSurfaces Object

## Description

The WorkSurfaces collection object represents all of the  objects associated with this part or component.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../WorkSurfaces/WorkSurfaces_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../WorkSurfaces/WorkSurfaces_Count.md) | Property that returns the number of items in this collection. |
| [Item](../WorkSurfaces/WorkSurfaces_Item.md) | Returns the specified WorkSurface object from the collection. This is the default property of the WorkSurfaces collection object. |
| [Parent](../WorkSurfaces/WorkSurfaces_Parent.md) | Property that returns the parent  object from whom this object can logically be reached. |
| [Type](../WorkSurfaces/WorkSurfaces_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[PartComponentDefinition.WorkSurfaces](../PartComponentDefinition/PartComponentDefinition_WorkSurfaces.md), [SheetMetalComponentDefinition.WorkSurfaces](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_WorkSurfaces.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Adding a new stitch (knit) feature](../../sample-programs/KnitFeature_Sample.md) | This sample demonstrates the creation of a stitch feature (known as the Knit feature in the API). The sample creates two work surfaces using surface extrusions and stitches them together. |

## Version

Introduced in version 6
