# DecalFeatures.Item Property

Parent Object: [DecalFeatures](../DecalFeatures/DecalFeatures.md)

## Description

Returns the specified DecalFeature object from the collection. This is the default property of the Decals collection object.

## Syntax

DecalFeatures.**Item**( ***Index*** As Variant ) As [DecalFeature](../DecalFeature/DecalFeature.md)

## Property Value

This is a read only property whose value is a [DecalFeature](../DecalFeature/DecalFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the DecalFeature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the decal's name. The name expected is the display name of the decal. This is the name that is displayed to the user in the assembly browser. If an out-of-range index or a name of a non-existent constraint name is provided, an error occurs. |

## Version

Introduced in version 6
