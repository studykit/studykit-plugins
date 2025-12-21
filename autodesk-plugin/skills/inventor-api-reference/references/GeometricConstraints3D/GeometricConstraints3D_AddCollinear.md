# GeometricConstraints3D.AddCollinear Method

Parent Object: [GeometricConstraints3D](../GeometricConstraints3D/GeometricConstraints3D.md)

## Description

Method that creates a new collinear constraint between the two input objects. This method will fail if the constraint overconstrains the sketch.

## Remarks

The constraint can currently be applied between two 3D sketch lines, or between a 3D sketch line and a work axis.

## Syntax

GeometricConstraints3D.**AddCollinear**( ***EntityOne*** As Object, ***EntityTwo*** As Object, [***Reserved1***] As Boolean, [***Reserved2***] As Boolean ) As [CollinearConstraint3D](../CollinearConstraint3D/CollinearConstraint3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | Object | Object that specifies the first entity to be constrained. |
| EntityTwo | Object | Object that specifies the second entity to be constrained. |
| Reserved1 | Boolean | This argument is reserved for future use and is currently ignored. |
| Reserved2 | Boolean | This argument is reserved for future use and is currently ignored.   This is an optional argument whose default value is True. |

## Version

Introduced in version 11
