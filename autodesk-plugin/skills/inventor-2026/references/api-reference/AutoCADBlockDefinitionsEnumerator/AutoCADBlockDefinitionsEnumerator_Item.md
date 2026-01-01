# AutoCADBlockDefinitionsEnumerator.Item Property

Parent Object: [AutoCADBlockDefinitionsEnumerator](../AutoCADBlockDefinitionsEnumerator/AutoCADBlockDefinitionsEnumerator.md)

## Description

Returns the specified AutoCADBlockDefinition object from the collection.

## Syntax

AutoCADBlockDefinitionsEnumerator.**Item**( ***Index*** As Variant ) As [AutoCADBlockDefinition](../AutoCADBlockDefinition/AutoCADBlockDefinition.md)

## Property Value

This is a read only property whose value is an [AutoCADBlockDefinition](../AutoCADBlockDefinition/AutoCADBlockDefinition.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the AutoCADBlockDefinition to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the AutoCADBlockDefinition name. If an out of range index or a name of a non-existent AutoCADBlockDefinition is provided, an error will occur. |

## Version

Introduced in version 2011
