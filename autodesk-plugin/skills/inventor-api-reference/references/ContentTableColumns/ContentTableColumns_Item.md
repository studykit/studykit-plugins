# ContentTableColumns.Item Property

Parent Object: [ContentTableColumns](../ContentTableColumns/ContentTableColumns.md)

## Description

Returns the specified ContentTableColumn object from the collection.

## Syntax

ContentTableColumns.**Item**( ***Index*** As Variant ) As [ContentTableColumn](../ContentTableColumn/ContentTableColumn.md)

## Property Value

This is a read only property whose value is a [ContentTableColumn](../ContentTableColumn/ContentTableColumn.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input value that specifies the ContentTableColumn object within the collection to return. Valid input is a Long to specify the index of the item within the collection where the first column has an index of 1. A String containing the name of the column can also be used; either the Name or DisplayHeading value can be used. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a Configuration Table](../../sample-programs/CustomTables_AddConfigurationTable_Sample.md) | This sample demonstrates the creation of a configuration (iPart/iAssembly) table in a drawing from a factory document. |

## Version

Introduced in version 2010
