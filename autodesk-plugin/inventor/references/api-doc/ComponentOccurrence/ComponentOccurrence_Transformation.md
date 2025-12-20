# ComponentOccurrence.Transformation Property

Parent Object: [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Description

Property that returns and sets the transformation for the occurrence. The transformation matrix defines the position and orientation of the component within the assembly. When setting the transform of an occurrence the actual change in position and orientation of the occurrence is limited by the constraints on the occurrence.

## Syntax

ComponentOccurrence.**Transformation**() As [Matrix](../Matrix/Matrix.md)

## Property Value

This is a read/write property whose value is a [Matrix](../Matrix/Matrix.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Assembly Move Occurrence](../../sample-programs/TransformOccurrence_Sample.md) | This sample demonstrates moving a component occurrence. This sample performs a translate, but a rotate can also be performed since the transform is defined using a matrix. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |