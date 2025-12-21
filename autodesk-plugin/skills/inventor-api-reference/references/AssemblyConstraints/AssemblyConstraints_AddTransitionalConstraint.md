# AssemblyConstraints.AddTransitionalConstraint Method

Parent Object: [AssemblyConstraints](../AssemblyConstraints/AssemblyConstraints.md)

## Description

Method that creates a new transitional constraint.

## Remarks

For transitional constraints, the bias point defines the position where the transition occurs to adjacent faces. Hence, the bias point must lie within the boundary of the input face. If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity. If this point is found not to lie within the face's boundary, a random sample point within the boundary is used.

## Syntax

AssemblyConstraints.**AddTransitionalConstraint**( ***FaceOne*** As [Face](../Face/Face.md), ***FaceTwo*** As [Face](../Face/Face.md), [***BiasPointOne***] As Variant, [***BiasPointTwo***] As Variant ) As [TransitionalConstraint](../TransitionalConstraint/TransitionalConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FaceOne | [Face](../Face/Face.md) | Input that defines the initial face on the first occurrence that is used in repositioning the occurrences. Once the constraint is placed, it can move along any of the faces of the part. |
| FaceTwo | [Face](../Face/Face.md) | Input that defines the initial face on the second occurrence that is used in repositioning the occurrences. Once the constraint is placed, it can move along any of the faces of the part. |
| BiasPointOne | Variant | Optional input object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint. An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other. If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity. |
| BiasPointTwo | Variant | Optional input object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint.   This is an optional argument whose default value is null. |

## Version

Introduced in version 5
