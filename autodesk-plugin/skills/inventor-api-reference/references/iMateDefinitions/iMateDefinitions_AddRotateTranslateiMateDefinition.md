# iMateDefinitions.AddRotateTranslateiMateDefinition Method

Parent Object: [iMateDefinitions](../iMateDefinitions/iMateDefinitions.md)

## Description

Method that creates a new rotate-translate motion iMate definition.

## Syntax

iMateDefinitions.**AddRotateTranslateiMateDefinition**( ***Entity*** As Object, ***Ratio*** As Variant, ***ForwardDirection*** As Boolean, [***BiasPoint***] As Variant, [***Name***] As String, [***MatchList***] As Variant ) As [RotateTranslateiMateDefinition](../RotateTranslateiMateDefinition/RotateTranslateiMateDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | Object | Defines the entity and its rotation axis. The input object must be a planar Face, a revolved Face, a linear Edge, a WorkPlane, or a WorkAxis object. For planar objects the rotation axis is normal to the input face. |
| Ratio | Variant | Input Variant that defines the distance of translation for every revolution of the rotated occurrence. This can be either a numeric value or a string. A parameter for this value is created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input the units can be specified as part of the string or will default to the current length units of the document. |
| ForwardDirection | Boolean | Defines the direction of translation with respect to the rotation direction relative to the axes directions. If the input value is True then when the rotation object is rotated in a positive direction about its axis, the translation object will move in the positive direction of its vector, If False, it will move in the negative direction. |
| BiasPoint | Variant | Point object that is used to help determine the initial position when this iMate definition is used. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint. An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other. If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity. |
| Name | String | Specifies the name of the iMate definition. If not specified, a name is automatically generated.   This is an optional argument whose default value is "". |
| MatchList | Variant | Array of Strings that specifies the priority order of the iMate definitions to match.   This is an optional argument whose default value is null. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |