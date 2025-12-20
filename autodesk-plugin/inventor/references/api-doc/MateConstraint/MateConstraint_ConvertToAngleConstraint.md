# MateConstraint.ConvertToAngleConstraint Method

Parent Object: [MateConstraint](../MateConstraint/MateConstraint.md)

## Description

Method that converts the constraint to an angle constraint, and returns the AngleConstraint object. This method can also be used to edit the geometries associated with an angle constraint without changing its type, in which case the same object is returned by the method.

## Syntax

MateConstraint.**ConvertToAngleConstraint**( ***EntityOne*** As Object, ***EntityTwo*** As Object, ***Angle*** As Variant, [***SolutionType***] As [AngleConstraintSolutionTypeEnum](../AngleConstraintSolutionTypeEnum.md), [***ReferenceVectorEntity***] As Variant, [***BiasPointOne***] As Variant, [***BiasPointTwo***] As Variant ) As [AngleConstraint](../AngleConstraint/AngleConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | Object | Input object that defines the first object. This object can be a planar face, work plane, linear edge, work axis, or a face that defines an axis. |
| EntityTwo | Object | Input object that defines the second object. This object can be a planar face, work plane, linear edge, work axis, or a face that defines an axis. |
| Angle | Variant | Input Variant that defines the angle between the two input entities. This can be either a numeric value or a string. A parameter for this value is created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input the units can be specified as part of the string or will default to the current angle units of the document. |
| SolutionType | [AngleConstraintSolutionTypeEnum](../AngleConstraintSolutionTypeEnum.md) | Optional input AngleConstraintSolutionTypeEnum that specifies the solution type. If specified to be kDirectedSolution, the solution always applies the right hand rule. If specified to be kUndirectedSolution, the solution allows either orientation, thus resolving situations where component orientation flips during a constraint drive or drag. If specified to be kReferenceVectorSolution, the ReferenceVectorEntity argument must be provided with a third entity for the solution. The default value is kDirectedSolution. |
| ReferenceVectorEntity | Variant | Optional input object that provides a third entity to solve the angle constraint. This argument is ignored if the SolutionType argument is not kReferenceVectorSolution. This object can be a planar face, work plane, linear edge, work axis, or a face that defines an axis.   This is an optional argument whose default value is null. |
| BiasPointOne | Variant | Optional input Point object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint. An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other. If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity.   This is an optional argument whose default value is null. |
| BiasPointTwo | Variant | Optional input Point object that is used help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the two bias points coincident. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint. An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other. If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |