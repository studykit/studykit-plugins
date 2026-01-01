# Vector.AddVector Method

Parent Object: [Vector](../Vector/Vector.md)

## Description

Add the specified vector to this vector.

## Syntax

Vector.**AddVector**( ***Argument*** As [Vector](../Vector/Vector.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Argument | [Vector](../Vector/Vector.md) | Input  to add. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |

## Version

Introduced in version 4
