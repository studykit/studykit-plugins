# DirectEditFeatures.Item Property

Parent Object: [DirectEditFeatures](../DirectEditFeatures/DirectEditFeatures.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

DirectEditFeatures.**Item**( ***Index*** As Variant ) As [DirectEditFeature](../DirectEditFeature/DirectEditFeature.md)

## Property Value

This is a read only property whose value is a [DirectEditFeature](../DirectEditFeature/DirectEditFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the DirectEditFeature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the DirectEditFeature name. If an out of range index or a name of a non-existent DirectEditFeature is provided, an error will occur. |

## Version

Introduced in version 2015
