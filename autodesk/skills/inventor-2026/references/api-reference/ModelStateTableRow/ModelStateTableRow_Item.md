# ModelStateTableRow.Item Property

Parent Object: [ModelStateTableRow](../ModelStateTableRow/ModelStateTableRow.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

ModelStateTableRow.**Item**( ***Index*** As Variant ) As [ModelStateTableCell](../ModelStateTableCell/ModelStateTableCell.md)

## Property Value

This is a read only property whose value is a [ModelStateTableCell](../ModelStateTableCell/ModelStateTableCell.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the ModelStateTableCell to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the column heading or the ModelStateTableColumn object. If an out-of-range index or a heading of a non-existent ModelStateTableColumn is provided, an error will occur. |

## Version

Introduced in version 2022
