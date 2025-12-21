# MirrorFeatures.Item Property

Parent Object: [MirrorFeatures](../MirrorFeatures/MirrorFeatures.md)

## Description

Returns the specified MirrorFeature objects from the collection. This is the default property of the MirrorFeatures collection object.

## Syntax

MirrorFeatures.**Item**( ***Index*** As Variant ) As [MirrorFeature](../MirrorFeature/MirrorFeature.md)

## Property Value

This is a read only property whose value is a [MirrorFeature](../MirrorFeature/MirrorFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the feature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the feature name. If an out of range index or a name of a non-existent feature is provided, an error occurs. |

## Version

Introduced in version 5
