# CustomTables Object

## Description

The CustomTables object contains the collection of objects for a given Sheet. See the Custom Tables overview for more information.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../CustomTables/CustomTables_Add.md) | Method that creates a new CustomTable. The new created CustomTable is returned. |
| [AddBendTableWithOptions](../CustomTables/CustomTables_AddBendTableWithOptions.md) | Method that creates a new bend table. The newly created CustomTable is returned. |
| [AddConfigurationTable](../CustomTables/CustomTables_AddConfigurationTable.md) | Method that creates a new configuration (iPart/iAssembly) table. The newly created CustomTable is returned. |
| [AddCSVTable](../CustomTables/CustomTables_AddCSVTable.md) | Method that creates a new custom table based on a CSV (comma delimited) file. The newly created CustomTable is returned. |
| [AddExcelTable](../CustomTables/CustomTables_AddExcelTable.md) | Method that creates a new custom table based on an excel file. The newly created CustomTable is returned. |
| [CreateTableFormat](../CustomTables/CustomTables_CreateTableFormat.md) | Method that creates a TableFormat object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CustomTables/CustomTables_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../CustomTables/CustomTables_Count.md) | Property that returns the number of items in this collection. |
| [Item](../CustomTables/CustomTables_Item.md) | Returns the specified object in the collection. |
| [Type](../CustomTables/CustomTables_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sheet.CustomTables](../Sheet/Sheet_CustomTables.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Custom Table - create](../../sample-programs/CustomTables_Sample.md) | This sample demonstrates how to create a custom table. |
| [Create a Bend Table](../../sample-programs/CustomTables_AddBendTable_Sample.md) | This sample demonstrates the creation of a bend table in a drawing from a sheet metal part. |
| [Create a Configuration Table](../../sample-programs/CustomTables_AddConfigurationTable_Sample.md) | This sample demonstrates the creation of a configuration (iPart/iAssembly) table in a drawing from a factory document. |
| [Create a drawing Excel Table](../../sample-programs/CustomTables_AddExcelTable_Sample.md) | This sample demonstrates the creation of a table based on an Excel file in a drawing. |

## Version

Introduced in version 9
