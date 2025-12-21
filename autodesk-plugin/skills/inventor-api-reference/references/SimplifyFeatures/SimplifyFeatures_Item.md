# SimplifyFeatures.Item Property

Parent Object: [SimplifyFeatures](../SimplifyFeatures/SimplifyFeatures.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

SimplifyFeatures.**Item**( ***Index*** As Variant ) As [SimplifyFeature](../SimplifyFeature/SimplifyFeature.md)

## Property Value

This is a read only property whose value is a [SimplifyFeature](../SimplifyFeature/SimplifyFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the SimplifyFeature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the SimplifyFeature name. If an out of range index or a name of a non-existent SimplifyFeature is provided, an error will occur. |

## Version

Introduced in version 2026
