# SurfaceBodies.Item Property

Parent Object: [SurfaceBodies](../SurfaceBodies/SurfaceBodies.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

SurfaceBodies.**Item**( ***Index*** As Long ) As [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Property Value

This is a read only property whose value is a [SurfaceBody](../SurfaceBody/SurfaceBody.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long value that specifies the index of the SurfaceBody to return. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Associative body copy](../../sample-programs/NonParametricBaseFeatures_AddByDefinition_Sample.md) | The following sample demonstrates copying bodies (associatively and non-associatively) across parts in an assembly. |
| [Sketch Add](../../sample-programs/PlanarSketches_Add_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.Add method. |
| [Sketch Add Oriented](../../sample-programs/PlanarSketches_AddWithOrientation_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.AddWithOrientation method. |

## Version

Introduced in version 4
