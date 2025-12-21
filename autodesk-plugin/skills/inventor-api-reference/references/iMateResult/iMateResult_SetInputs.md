# iMateResult.SetInputs Method

Parent Object: [iMateResult](../iMateResult/iMateResult.md)

## Description

Method that edits the inputs of an iMate result.

## Syntax

iMateResult.**SetInputs**( ***iMateDefinition*** As [iMateDefinition](../iMateDefinition/iMateDefinition.md), ***Entity*** As Object, [***EntityBiasPoint***] As Variant, [***SolutionType***] As [AngleConstraintSolutionTypeEnum](../AngleConstraintSolutionTypeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| iMateDefinition | [iMateDefinition](../iMateDefinition/iMateDefinition.md) | Input iMateDefinitionProxy object that defines the input iMate. |
| Entity | Object | Input object that defines the second entity. This object can be either a iMateDefinition proxy object or a geometric entity. |
| EntityBiasPoint | Variant | Optional input Point object that is used to help in determining the initial position of the occurrence. The occurrences are repositioned in an attempt to make the bias point coincident with the iMate. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint.  An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias point you can define the position of the two occurrences, relative to each other.  If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity. |
| SolutionType | [AngleConstraintSolutionTypeEnum](../AngleConstraintSolutionTypeEnum.md) | Optional input AngleConstraintSolutionTypeEnum that specifies the solution type when creating an angle constraint. If specified to be kDirectedSolution, the solution always applies the right hand rule. If specified to be kUndirectedSolution, the solution allows either orientation, thus resolving situations where component orientation flips during a constraint drive or drag. The default value is kDirectedSolution.   This is an optional argument whose default value is 78593. |

## Version

Introduced in version 2011
