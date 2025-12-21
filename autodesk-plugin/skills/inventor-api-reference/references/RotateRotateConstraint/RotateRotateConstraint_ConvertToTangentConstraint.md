# RotateRotateConstraint.ConvertToTangentConstraint Method

Parent Object: [RotateRotateConstraint](../RotateRotateConstraint/RotateRotateConstraint.md)

## Description

Method that converts the constraint to a tangent constraint, and returns the TangentConstraint object. This method can also be used to edit the geometries associated with a tangent constraint without changing its type, in which case the same object is returned by the method.

## Syntax

RotateRotateConstraint.**ConvertToTangentConstraint**( ***EntityOne*** As Object, ***EntityTwo*** As Object, ***InsideTangency*** As Boolean, ***Offset*** As Variant, [***BiasPointOne***] As Variant, [***BiasPointTwo***] As Variant ) As [TangentConstraint](../TangentConstraint/TangentConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | Object | Input object that defines the first object. |
| EntityTwo | Object | Input object that defines the second object. This object is a circular edge. |
| InsideTangency | Boolean | Input Boolean that specifies the orientation of the surfaces at the tangent contact point of the surfaces. |
| Offset | Variant | Input Variant that defines the offset between the two input entities. This can be either a numeric value or a string. A parameter for this value is created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input the units can be specified as part of the string or will default to the current length units of the document. |
| BiasPointOne | Variant | Optional input Point object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint.  An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other.  If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity. |
| BiasPointTwo | Variant | Optional input Point object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint.  An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other.  If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity.    This is an optional argument whose default value is null. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |