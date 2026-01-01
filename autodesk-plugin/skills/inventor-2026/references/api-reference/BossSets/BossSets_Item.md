# BossSets.Item Property

Parent Object: [BossSets](../BossSets/BossSets.md)

## Description

Property that returns an item from the collection. You can provide either the index of the item in the collection, where the first item is index 1, or you can provide the name of the object.

## Syntax

BossSets.**Item**( ***Index*** As Long ) As [BossSet](../BossSet/BossSet.md)

## Property Value

This is a read only property whose value is a [BossSet](../BossSet/BossSet.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Variant value that specifies the feature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a String indicating the feature name. If an out of range index or a name of a non-existent feature is provided, an error occurs. |

## Version

Introduced in version 2012
