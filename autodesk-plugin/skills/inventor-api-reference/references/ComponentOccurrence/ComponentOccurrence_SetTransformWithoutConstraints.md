# ComponentOccurrence.SetTransformWithoutConstraints Method

Parent Object: [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Description

Method that sets the position and orientation of the occurrence, ignoring any constraints on the occurrence. When the assembly is recomputed the occurrence will reposition to honor the constraints.

## Syntax

ComponentOccurrence.**SetTransformWithoutConstraints**( ***Matrix*** As [Matrix](../Matrix/Matrix.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Matrix | [Matrix](../Matrix/Matrix.md) | Input object that specifies the position and orientation of the occurrence. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Assembly Move Occurrence](../../sample-programs/TransformOccurrence_Sample.md) | This sample demonstrates moving a component occurrence. This sample performs a translate, but a rotate can also be performed since the transform is defined using a matrix. |

## Version

Introduced in version 5
