# AssetTexture.Item Property

Parent Object: [AssetTexture](../AssetTexture/AssetTexture.md)

## Description

Read-only property that returns the specified AssetValue object from the asset.

## Syntax

AssetTexture.**Item**( ***Index*** As Variant ) As [AssetValue](../AssetValue/AssetValue.md)

## Property Value

This is a read only property whose value is an [AssetValue](../AssetValue/AssetValue.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the value to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the asset value name. If an out of range index or a name of a non-existent asset value is provided, an error will occur.  The first item in the collection has an index of 1. |

## Version

Introduced in version 2014
