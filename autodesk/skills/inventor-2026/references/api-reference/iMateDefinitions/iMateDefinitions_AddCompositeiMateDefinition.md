# iMateDefinitions.AddCompositeiMateDefinition Method

Parent Object: [iMateDefinitions](../iMateDefinitions/iMateDefinitions.md)

## Description

Method that creates a new composite iMate definition. The newly created CompositeiMateDefinition object is returned. When iMate definition objects are used as input for a composite iMate, the iMateDefinition objects are no longer directly accessible through the iMateDefinitions collection. They are only accessible through the CompositeiMateDefinition object.

## Syntax

iMateDefinitions.**AddCompositeiMateDefinition**( ***iMates*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***Name***] As String, [***MatchList***] As Variant ) As [CompositeiMateDefinition](../CompositeiMateDefinition/CompositeiMateDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| iMates | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Contains the iMates that are used as input for the composite iMate. The collection must contain only iMateDefinition objects. It will fail if any other object types are input or if any of the objects are a CompositeiMateDefinition object. |
| Name | String | Specifies the name of the iMate definition. If not specified, a name is automatically generated. |
| MatchList | Variant | Array of Strings that specifies the priority order of the iMate definitions to match.   This is an optional argument whose default value is null. |

## Version

Introduced in version 11
