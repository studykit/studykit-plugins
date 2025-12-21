# FlushConstraintProxy.ConvertToRotateTranslateConstraint Method

Parent Object: [FlushConstraintProxy](../FlushConstraintProxy/FlushConstraintProxy.md)

## Description

Method that converts the constraint to a rotate-translate constraint, and returns the RotateTranslateConstraint object. This method can also be used to edit the geometries associated with a rotate-translate constraint without changing its type, in which case the same object is returned by the method.

## Syntax

FlushConstraintProxy.**ConvertToRotateTranslateConstraint**( ***EntityOne*** As Object, ***EntityTwo*** As Object, ***Ratio*** As Variant, ***ForwardDirection*** As Boolean, [***BiasPointOne***] As Variant, [***BiasPointTwo***] As Variant ) As [RotateTranslateConstraint](../RotateTranslateConstraint/RotateTranslateConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | Object | Input object that defines the first object and its rotation axis. The input object must be a planar Face, a revolved Face, a linear Edge, a WorkPlane, or a WorkAxis object. For planar objects the rotation axis is normal to the input face. |
| EntityTwo | Object | Input object that defines the second object and its translation axis. The input object must be a planar Face, a revolved Face, a linear Edge, a WorkPlane, or a WorkAxis object. For planar objects the translation axis is normal to the input face. |
| Ratio | Variant | Input Variant that defines the distance of translation for every revolution of the rotated occurrence. This can be either a numeric value or a string. A parameter for this value is created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input the units can be specified as part of the string or will default to the current length units of the document. |
| ForwardDirection | Boolean | Input Boolean that defines the direction of translation with respect to the rotation direction relative to the axes directions. If the input value is True then when the rotation object is rotated in a positive direction about its axis, the translation object will move in the positive direction of its vector, If False, it will move in the negative direction. |
| BiasPointOne | Variant | Optional input Point object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint.  An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other.  If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity. |
| BiasPointTwo | Variant | Optional input Point object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint.  An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other.  If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity.    This is an optional argument whose default value is null. |

## Version

Introduced in version 2011
