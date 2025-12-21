# GeometricConstraints3D.AddParallel Method

Parent Object: [GeometricConstraints3D](../GeometricConstraints3D/GeometricConstraints3D.md)

## Description

Method that creates a new parallel constraint between the two input entities. This method will fail if the constraint overconstrains the sketch.

## Remarks

The constraint can currently be applied between: \* a 3D sketch line and another 3D sketch line, a work axis, linear edge, or axis of a cylindrical face. \* a 3D sketch line and a planar face or work plane.

## Syntax

GeometricConstraints3D.**AddParallel**( ***EntityOne*** As Object, ***EntityTwo*** As Object, [***Reserved1***] As Boolean, [***Reserved2***] As Boolean ) As [ParallelConstraint3D](../ParallelConstraint3D/ParallelConstraint3D.md)

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

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |