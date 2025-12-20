# WorkSurfaces.Item Property

Parent Object: [WorkSurfaces](../WorkSurfaces/WorkSurfaces.md)

## Description

Returns the specified WorkSurface object from the collection. This is the default property of the WorkSurfaces collection object.

## Syntax

WorkSurfaces.**Item**( ***Index*** As Variant ) As [WorkSurface](../WorkSurface/WorkSurface.md)

## Property Value

This is a read only property whose value is a [WorkSurface](../WorkSurface/WorkSurface.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the object to return. This can be a numeric value indicating the index of the item in the collection or it can be a string indicating the work surface name. If an out of range index or a name of a non-existent work surface is specified, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Adding a new stitch (knit) feature](../../sample-programs/KnitFeature_Sample.md) | This sample demonstrates the creation of a stitch feature (known as the Knit feature in the API). The sample creates two work surfaces using surface extrusions and stitches them together. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |