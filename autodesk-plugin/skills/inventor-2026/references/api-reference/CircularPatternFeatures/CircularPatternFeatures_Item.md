# CircularPatternFeatures.Item Property

Parent Object: [CircularPatternFeatures](../CircularPatternFeatures/CircularPatternFeatures.md)

## Description

Returns the specified CircularPatternFeature object from the collection. This is the default property of the CircularPatternFeatures collection object.

## Syntax

CircularPatternFeatures.**Item**( ***Index*** As Variant ) As [CircularPatternFeature](../CircularPatternFeature/CircularPatternFeature.md)

## Property Value

This is a read only property whose value is a [CircularPatternFeature](../CircularPatternFeature/CircularPatternFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the feature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the feature name. If an out of range index or a name of a non-existent feature is provided, an error occurs. |

## Version

Introduced in version 5
