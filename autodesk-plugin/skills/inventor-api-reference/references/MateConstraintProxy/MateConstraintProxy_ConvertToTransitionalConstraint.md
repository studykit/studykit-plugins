# MateConstraintProxy.ConvertToTransitionalConstraint Method

Parent Object: [MateConstraintProxy](../MateConstraintProxy/MateConstraintProxy.md)

## Description

Method that converts the constraint to a transitional constraint, and returns the TransitionalConstraint object. This method can also be used to edit the geometries associated with a transitional constraint without changing its type, in which case the same object is returned by the method.

## Syntax

MateConstraintProxy.**ConvertToTransitionalConstraint**( ***FaceOne*** As [Face](../Face/Face.md), ***FaceTwo*** As [Face](../Face/Face.md), [***BiasPointOne***] As Variant, [***BiasPointTwo***] As Variant ) As [TransitionalConstraint](../TransitionalConstraint/TransitionalConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FaceOne | [Face](../Face/Face.md) | First input face that defines the initial face that is used in repositioning the parts. Once the constraint is placed it can move along any of the faces of the part. |
| FaceTwo | [Face](../Face/Face.md) | Second input face that defines the initial face that is used in repositioning the parts. Once the constraint is placed it can move along any of the faces of the part. |
| BiasPointOne | Variant | Optional input Point object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint.  An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other.  If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity. |
| BiasPointTwo | Variant | Optional input Point object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint.  An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other.  If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity.    This is an optional argument whose default value is null. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |