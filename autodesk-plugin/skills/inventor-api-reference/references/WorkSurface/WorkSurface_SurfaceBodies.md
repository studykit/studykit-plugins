# WorkSurface.SurfaceBodies Property

Parent Object: [WorkSurface](../WorkSurface/WorkSurface.md)

## Description

Property that returns the surface bodies associated with this work surface. A work surface can contain more than one surface body.

## Syntax

WorkSurface.**SurfaceBodies**() As [SurfaceBodies](../SurfaceBodies/SurfaceBodies.md)

## Property Value

This is a read only property whose value is a [SurfaceBodies](../SurfaceBodies/SurfaceBodies.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |