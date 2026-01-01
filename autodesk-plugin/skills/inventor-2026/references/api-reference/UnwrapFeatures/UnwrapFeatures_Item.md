# UnwrapFeatures.Item Property

Parent Object: [UnwrapFeatures](../UnwrapFeatures/UnwrapFeatures.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

UnwrapFeatures.**Item**( ***Index*** As Variant ) As [UnwrapFeature](../UnwrapFeature/UnwrapFeature.md)

## Property Value

This is a read only property whose value is a [UnwrapFeature](../UnwrapFeature/UnwrapFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the UnwrapFeature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the UnwrapFeature name. If an out of range index or a name of a non-existent UnwrapFeature is provided, an error will occur. |

## Version

Introduced in version 2020
