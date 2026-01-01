# ImportedModelEntities.Item Property

Parent Object: [ImportedModelEntities](../ImportedModelEntities/ImportedModelEntities.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

ImportedModelEntities.**Item**( ***Index*** As Variant ) As [ImportedModelEntity](../ImportedModelEntity/ImportedModelEntity.md)

## Property Value

This is a read only property whose value is an [ImportedModelEntity](../ImportedModelEntity/ImportedModelEntity.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the ImportedModelEntity to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the ImportedModelEntity name. If an out of range index or a name of a non-existent ImportedModelEntity is provided, an error will occur. |

## Version

Introduced in version 2016
