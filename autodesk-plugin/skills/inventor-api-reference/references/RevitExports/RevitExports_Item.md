# RevitExports.Item Property

Parent Object: [RevitExports](../RevitExports/RevitExports.md)

## Description

Allows integer-indexed access to items in the collection.

## Syntax

RevitExports.**Item**( ***Index*** As Variant ) As [RevitExport](../RevitExport/RevitExport.md)

## Property Value

This is a read only property whose value is a [RevitExport](../RevitExport/RevitExport.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the RevitExport to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the RevitExport name. If an out of range index or a name of a non-existent RevitExport is provided, an error occurs. |

## Version

Introduced in version 2022
