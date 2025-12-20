# ConstraintLimits.Minimum Property

Parent Object: [ConstraintLimits](../ConstraintLimits/ConstraintLimits.md)

## Description

Property that returns the Parameter object that controls the minimum limit value. This property returns Nothing if the minimum limit has never been enabled for this constraint or the parameter associated with the minimum value was deleted. Set the MinimumEnabled property to True to make this parameter available.

## Syntax

ConstraintLimits.**Minimum**() As [Parameter](../Parameter/Parameter.md)

## Property Value

This is a read only property whose value is a [Parameter](../Parameter/Parameter.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add mate constraint with limits](../../sample-programs/AssemblyConstraints_AddMateConstraint3_Sample.md) | This sample demonstrates the creation of an assembly mate constraint with maximum and minimum limits defined. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |