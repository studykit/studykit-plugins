# ConstraintLimits.Maximum Property

Parent Object: [ConstraintLimits](../ConstraintLimits/ConstraintLimits.md)

## Description

Property that returns the Parameter object that controls the maximum limit value. This property returns Nothing if the maximum limit has never been enabled for this constraint or the parameter associated with the maximum value was deleted. Set the MaximumEnabled property to True to make this parameter available.

## Syntax

ConstraintLimits.**Maximum**() As [Parameter](../Parameter/Parameter.md)

## Property Value

This is a read only property whose value is a [Parameter](../Parameter/Parameter.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add mate constraint with limits](../../sample-programs/AssemblyConstraints_AddMateConstraint3_Sample.md) | This sample demonstrates the creation of an assembly mate constraint with maximum and minimum limits defined. |

## Version

Introduced in version 2011
