# ContentTableRow.GetCellValue Method

Parent Object: [ContentTableRow](../ContentTableRow/ContentTableRow.md)

## Description

This method returns value of cell specified by given index. Caller can specify particular custom parameters which will be used for expression evaluation.

## Syntax

ContentTableRow.**GetCellValue**( ***CellIndex*** As Variant, [***CustomInput***] As Variant ) As String

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CellIndex | Variant | Input Variant value that specifies the ContentTableCell object within the collection to return. Valid index values are 1 to the value of Count, ContentTableColumn object or column internal name. |
| CustomInput | Variant | Optional input NameValueMap that specifies the input to use for the custom input. If the family is custom and this is not supplied, the default values for custom values are used. For each input value you use the NameValueMap to specify the Column ID as the name and the custom value as the new value . If the factory is not a custom factory this argument is ignored. |

## Version

Introduced in version 2011
