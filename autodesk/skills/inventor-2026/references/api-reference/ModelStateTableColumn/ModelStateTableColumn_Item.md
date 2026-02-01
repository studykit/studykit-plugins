# ModelStateTableColumn.Item Property

Parent Object: [ModelStateTableColumn](../ModelStateTableColumn/ModelStateTableColumn.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

ModelStateTableColumn.**Item**( ***Index*** As Variant ) As [ModelStateTableCell](../ModelStateTableCell/ModelStateTableCell.md)

## Property Value

This is a read only property whose value is a [ModelStateTableCell](../ModelStateTableCell/ModelStateTableCell.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input value that specifies the ModelStateTableCell to return. This can be either a numeric value indicating the index of a row where the first row has an index of 1 or it can be a string indicating the member name of a particular row. The member name is obtained using the MemberName property on an ModelStateTableRow object. If an out of range index or a name of a non-existent member is provided, an error will occur |

## Version

Introduced in version 2022
