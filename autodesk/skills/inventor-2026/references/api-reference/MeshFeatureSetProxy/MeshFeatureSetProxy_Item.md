# MeshFeatureSetProxy.Item Property

Parent Object: [MeshFeatureSetProxy](../MeshFeatureSetProxy/MeshFeatureSetProxy.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

MeshFeatureSetProxy.**Item**( ***Index*** As Variant ) As [MeshFeature](../MeshFeature/MeshFeature.md)

## Property Value

This is a read only property whose value is a [MeshFeature](../MeshFeature/MeshFeature.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the MeshFeature to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the MeshFeature name. If an out of range index or a name of a non-existent name is provided, an error occurs. |

## Version

Introduced in version 2017
