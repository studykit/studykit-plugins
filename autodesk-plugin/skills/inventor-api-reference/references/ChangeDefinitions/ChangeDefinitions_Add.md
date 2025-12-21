# ChangeDefinitions.Add Method

Parent Object: [ChangeDefinitions](../ChangeDefinitions/ChangeDefinitions.md)

## Description

Method that creates a new ChangeDefinition. The newly created ChangeDefinition is returned.

## Syntax

ChangeDefinitions.**Add**( ***InternalName*** As String, ***CommandName*** As String ) As [ChangeDefinition](../ChangeDefinition/ChangeDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InternalName | String | Input String that defines the name of the new ChangeDefinition. The name specified must be unique with respect to the other change definitions in the collection. If a unique name is not specified, an error will occur. |
| CommandName | String | Input String that defines the localized command name that will show up in the undo list. |

## Version

Introduced in version 9
