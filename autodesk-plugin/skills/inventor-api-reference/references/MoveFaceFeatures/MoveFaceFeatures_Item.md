# MoveFaceFeatures.Item Property

Parent Object: [MoveFaceFeatures](../MoveFaceFeatures/MoveFaceFeatures.md)

## Description

Returns the specified feature object from the collection. This is the default property of this collection object.

## Syntax

MoveFaceFeatures.**Item**( ***Index*** As Variant ) As [MoveFaceFeature](../MoveFaceFeature/MoveFaceFeature.md)

## Property Value

This is a read only property whose value is a [MoveFaceFeature](../MoveFaceFeature/MoveFaceFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the feature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the feature name. If an out of range index or a name of a non-existent feature is provided, an error occurs. |

## Version

Introduced in version 10
