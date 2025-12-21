# RevisionClouds.Item Property

Parent Object: [RevisionClouds](../RevisionClouds/RevisionClouds.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

RevisionClouds.**Item**( ***Index*** As Variant ) As [RevisionCloud](../RevisionCloud/RevisionCloud.md)

## Property Value

This is a read only property whose value is a [RevisionCloud](../RevisionCloud/RevisionCloud.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the RevisionCloud to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the RevisionCloud name. If an out of range index or a name of a non-existent RevisionCloud is provided, an error will occur . |

## Version

Introduced in version 2024
