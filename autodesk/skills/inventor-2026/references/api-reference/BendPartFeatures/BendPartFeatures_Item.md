# BendPartFeatures.Item Property

Parent Object: [BendPartFeatures](../BendPartFeatures/BendPartFeatures.md)

## Description

Returns the specified BendPartFeature object from the collection. This is the default property of the BendPartFeatures collection object.

## Syntax

BendPartFeatures.**Item**( ***Index*** As Variant ) As [BendPartFeature](../BendPartFeature/BendPartFeature.md)

## Property Value

This is a read only property whose value is a [BendPartFeature](../BendPartFeature/BendPartFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Value that specifies the index of the BendPartFeature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the attribute set name. If an out-of-range index or a name of a nonexistent attribute set is provided, an error occurs. |

## Version

Introduced in version 2008
