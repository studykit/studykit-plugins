# FeatureDimensions.Item Property

Parent Object: [FeatureDimensions](../FeatureDimensions/FeatureDimensions.md)

## Description

Returns the specified FeatureDimension object from the collection.

## Syntax

FeatureDimensions.**Item**( ***Index*** As Variant ) As [FeatureDimension](../FeatureDimension/FeatureDimension.md)

## Property Value

This is a read only property whose value is a [FeatureDimension](../FeatureDimension/FeatureDimension.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the FeatureDimension to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the name of the parameter associated with the dimension. If an out of range index or a name of a non-existent FeatureDimension is provided, an error will occur. |

## Version

Introduced in version 2008
