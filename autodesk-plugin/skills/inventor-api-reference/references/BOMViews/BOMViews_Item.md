# BOMViews.Item Property

Parent Object: [BOMViews](../BOMViews/BOMViews.md)

## Description

Returns the specified BOMView object from the collection.

## Syntax

BOMViews.**Item**( ***Index*** As Variant ) As [BOMView](../BOMView/BOMView.md)

## Property Value

This is a read only property whose value is a [BOMView](../BOMView/BOMView.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the BOMView to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the name of a BOMView. If an out of range index or a name of a non-existent BOMView is provided, an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Using the BOM APIs](../../sample-programs/BOM_Sample.md) | This sample demonstrates the Bill of Materials API functionality in assemblies. |
| [Exporting the assembly BOM](../../sample-programs/BOMView_Export_Sample.md) | This sample demonstrates exporting the Assembly BOM to an external file. |

## Version

Introduced in version 10
