# ThreadFeatures.Item Property

Parent Object: [ThreadFeatures](../ThreadFeatures/ThreadFeatures.md)

## Description

Returns the specified ThreadFeature object from the collection. This is the default property of the ThreadFeatures collection object.

## Syntax

ThreadFeatures.**Item**( ***Index*** As Variant ) As [ThreadFeature](../ThreadFeature/ThreadFeature.md)

## Property Value

This is a read only property whose value is a [ThreadFeature](../ThreadFeature/ThreadFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the feature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the feature name. If an out of range index or a name of a non-existent feature is provided, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Edit thread features](../../sample-programs/ThreadFeatures_CreateStandardThreadInfo_Sample.md) | The following example demonstrates how to edit an existing thread feature. |

## Version

Introduced in version 5
