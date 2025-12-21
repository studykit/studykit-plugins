# TableParameters.Item Property

Parent Object: [TableParameters](../TableParameters/TableParameters.md)

## Description

Returns the specified TableParameter object from the collection. This is the default property of the TableParameters collection object.

## Syntax

TableParameters.**Item**( ***Index*** As Variant ) As [TableParameter](../TableParameter/TableParameter.md)

## Property Value

This is a read only property whose value is a [TableParameter](../TableParameter/TableParameter.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the TableParameter to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the parameter name. If an out of range index or a name of a non-existent parameter is provided, an error occurs. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Table Parameters](../../sample-programs/ParameterTables_Sample.md) | This sample demonstrates how to access the Parameters object, and from it in turn the TableParameters collection that represents the collection of parameters that have been linked/embedded from an external spreadsheet. |

## Version

Introduced in version 4
