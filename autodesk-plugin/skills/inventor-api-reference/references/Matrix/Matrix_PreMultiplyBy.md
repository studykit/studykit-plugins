# Matrix.PreMultiplyBy Method

Parent Object: [Matrix](../Matrix/Matrix.md)

## Description

Method that post-multiplies this matrix by the specified matrix, setting this matrix to the result.

## Syntax

Matrix.**PreMultiplyBy**( ***Matrix*** As [Matrix](../Matrix/Matrix.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Matrix | [Matrix](../Matrix/Matrix.md) | Input Matrix object that specifies the matrix to pre-multiply by. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |