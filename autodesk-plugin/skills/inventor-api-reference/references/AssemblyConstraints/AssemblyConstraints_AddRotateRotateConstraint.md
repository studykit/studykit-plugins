# AssemblyConstraints.AddRotateRotateConstraint Method

Parent Object: [AssemblyConstraints](../AssemblyConstraints/AssemblyConstraints.md)

## Description

Method that creates a new rotation motion constraint.

## Syntax

AssemblyConstraints.**AddRotateRotateConstraint**( ***EntityOne*** As Object, ***EntityTwo*** As Object, ***Ratio*** As Variant, ***ForwardDirection*** As Boolean, [***BiasPointOne***] As Variant, [***BiasPointTwo***] As Variant ) As [RotateRotateConstraint](../RotateRotateConstraint/RotateRotateConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | Object | Input object that defines the first object and its rotation axis. The input object must be a planar , a revolved Point, a linear Edge, a WorkPlane, or a WorkAxis object. For planar objects the rotation axis is normal to the input face. |
| EntityTwo | Object | Input object that defines the second object and its rotation axis. The input object must be a planar , a revolved Face, a linear Edge, a WorkPlane, or a WorkAxis object. |
| Ratio | Variant | Input Variant that defines the rotation ratio between the two input entities. This can be either a numeric value or a string. A parameter for this value is created and the supplied string or value is assigned to the parameter. The input value is unitless. |
| ForwardDirection | Boolean | Input Boolean that defines the direction of rotation of the objects with respect to the axis direction. If the input value is True then both objects will rotate the same direction around their axes. If False, then they will rotate in opposite directions. |
| BiasPointOne | Variant | Optional input object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint. An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other. If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity. |
| BiasPointTwo | Variant | Optional input object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint. An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other. If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity.   This is an optional argument whose default value is null. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |