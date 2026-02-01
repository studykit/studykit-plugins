# iMateDefinitions.AddAngleiMateDefinition Method

Parent Object: [iMateDefinitions](../iMateDefinitions/iMateDefinitions.md)

## Description

Method that creates a new angle iMate definition. The newly created AngleiMateDefinition object is returned.

## Syntax

iMateDefinitions.**AddAngleiMateDefinition**( ***Entity*** As Object, ***DirectionReversed*** As Boolean, ***Angle*** As Variant, [***BiasPoint***] As Variant, [***Name***] As String, [***MatchList***] As Variant ) As [AngleiMateDefinition](../AngleiMateDefinition/AngleiMateDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | Object | Object that defines the entity. This object can be a planar face, work plane, linear edge, work axis, or a face that defines an axis. |
| DirectionReversed | Boolean | Boolean that specifies whether to reverse the direction of the entity. |
| Angle | Variant | Defines the angle value. This can be either a numeric value or a string. A parameter for this value is created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input the units can be specified as part of the string or will default to the current angle units of the document. |
| BiasPoint | Variant | Point object that is used to help determine the initial position when this iMate definition is used. This provides some general control over the position of the occurrence when it isn't being controlled by another constraint. An example of when the bias points are useful is the case when the first constraint on a part is a mate constraint. In the case where the mate is between two planes, the parts can be positioned anywhere along the infinite plane that defines their mating contact. Using the bias points you can define the position of the two occurrences, relative to each other. If a bias point is not given, one is calculated that is at the center of the parameter range of the input entity. |
| Name | String | String that specifies the name of the iMate definition. If not specified, a name is automatically generated.   This is an optional argument whose default value is "". |
| MatchList | Variant | Array of Strings that specifies the priority order of the iMate definitions to match.   This is an optional argument whose default value is null. |

## Version

Introduced in version 11
