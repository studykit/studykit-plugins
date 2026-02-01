# iAssemblyTableColumn.Item Property

Parent Object: [iAssemblyTableColumn](../iAssemblyTableColumn/iAssemblyTableColumn.md)

## Description

Returns the specified iAssemblyTableCell object from the collection.

## Syntax

iAssemblyTableColumn.**Item**( ***Index*** As Variant ) As [iAssemblyTableCell](../iAssemblyTableCell/iAssemblyTableCell.md)

## Property Value

This is a read only property whose value is an [iAssemblyTableCell](../iAssemblyTableCell/iAssemblyTableCell.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Value that specifies the iAssemblyTableCell to return. This can be either a numeric value indicating the index of a row where the first row has an index of 1 or it can be a string indicating the member name of a particular row. The member name is obtained using the MemberName property on an iAssemblyTableRow object. If an out of range index or a name of a non-existent member is provided, an error will occur |

## Version

Introduced in version 11
