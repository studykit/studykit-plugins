# iMateDefinitions.AddInsertiMateDefinition Method

Parent Object: [iMateDefinitions](../iMateDefinitions/iMateDefinitions.md)

## Description

Method that creates a new insert iMate definition. The newly created InsertiMateDefinition object is returned.

## Syntax

iMateDefinitions.**AddInsertiMateDefinition**( ***Entity*** As Object, ***AxesOpposed*** As Boolean, ***Distance*** As Variant, [***BiasPoint***] As Variant, [***Name***] As String, [***MatchList***] As Variant ) As [InsertiMateDefinition](../InsertiMateDefinition/InsertiMateDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | Object | Object that defines the entity. This object must be a circular edge. |
| AxesOpposed | Boolean | Specifies whether the direction of the axis of the input entities are in the same direction or opposed. A value of True indicates they are opposed. |
| Distance | Variant | Defines the offset value. This can be either a numeric value or a string. A parameter for this value is created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input the units can be specified as part of the string or will default to the current length units of the document. |
| BiasPoint | Variant | Used to help determine the initial position when this iMate definition is used. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint. An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other. If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity. |
| Name | String | Specifies the name of the iMate definition. If not specified, a name is automatically generated.   This is an optional argument whose default value is "". |
| MatchList | Variant | Array of Strings that specifies the priority order of the iMate definitions to match.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add iMate Definition](../../sample-programs/iMateDefinitions_AddMateiMateDefinition_Sample.md) | Add iMate definitions using AddMateiMateDefinition and AddInsertiMateDefinition. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |