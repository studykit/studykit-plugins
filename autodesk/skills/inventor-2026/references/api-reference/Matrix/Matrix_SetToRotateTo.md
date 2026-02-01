# Matrix.SetToRotateTo Method

Parent Object: [Matrix](../Matrix/Matrix.md)

## Description

Sets to the matrix of rotation that would align the 'from' vector with the 'to' vector. The optional Axis argument may be used when the two vectors are parallel and in opposite directions to specify a specific solution, but is otherwise ignored.

## Remarks

Although the last argument is optional, a NULL (Nothing for VB users) must be passed in if the user wishes to ignore the argument.

## Syntax

Matrix.**SetToRotateTo**( ***From*** As [Vector](../Vector/Vector.md), ***To*** As [Vector](../Vector/Vector.md), [***Axis***] As [Vector](../Vector/Vector.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| From | [Vector](../Vector/Vector.md) | Input Vector object to align from. |
| To | [Vector](../Vector/Vector.md) | Input Vector object to align to. |
| Axis | [Vector](../Vector/Vector.md) | Input Vector object. |

## Version

Introduced in version 4
