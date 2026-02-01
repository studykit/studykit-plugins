# ExtendFeatures.Item Property

Parent Object: [ExtendFeatures](../ExtendFeatures/ExtendFeatures.md)

## Description

Property that returns an item from the collection. You can provide either the index of the item in the collection, where the first item is index 1, or you can provide the name of the object.

## Syntax

ExtendFeatures.**Item**( ***Index*** As Variant ) As [ExtendFeature](../ExtendFeature/ExtendFeature.md)

## Property Value

This is a read only property whose value is an [ExtendFeature](../ExtendFeature/ExtendFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the feature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a String indicating the feature name. If an out of range index or a name of a non-existent feature is provided, an error occurs. |

## Version

Introduced in version 11
