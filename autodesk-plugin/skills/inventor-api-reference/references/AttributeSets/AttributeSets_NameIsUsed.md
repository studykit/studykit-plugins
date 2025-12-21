# AttributeSets.NameIsUsed Property

Parent Object: [AttributeSets](../AttributeSets/AttributeSets.md)

## Description

Property that returns whether an existing attribute set has the specified name or not. Multiple AttributeSets with the same name are not allowed within this collection. Returns True if the name is already being used.

## Syntax

AttributeSets.**NameIsUsed**( ***AttributeSetName*** As String ) As Boolean

## Property Value

This is a read only property whose value is a Boolean.

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AttributeSetName | String | Input String value containing the attribute set name to check. |

## Version

Introduced in version 5
