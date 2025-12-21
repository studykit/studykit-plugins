# BendFeatures.Item Property

Parent Object: [BendFeatures](../BendFeatures/BendFeatures.md)

## Description

Returns the specified BendFeature object from the collection. This is the default property of the BendFeatures collection object.

## Syntax

BendFeatures.**Item**( ***Index*** As Variant ) As [BendFeature](../BendFeature/BendFeature.md)

## Property Value

This is a read only property whose value is a [BendFeature](../BendFeature/BendFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Long value that specifies the index of the to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the attribute set name. If an out-of-range index or a name of a nonexistent attribute set is provided, an error occurs. |

## Version

Introduced in version 5.3
