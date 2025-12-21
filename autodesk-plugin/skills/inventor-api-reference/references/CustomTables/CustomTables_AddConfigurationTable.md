# CustomTables.AddConfigurationTable Method

Parent Object: [CustomTables](../CustomTables/CustomTables.md)

## Description

Method that creates a new configuration (iPart/iAssembly) table. The newly created CustomTable is returned.

## Syntax

CustomTables.**AddConfigurationTable**( ***ConfigurationFileName*** As String, ***PlacementPoint*** As [Point2d](../Point2d/Point2d.md), [***Title***] As String, [***Columns***] As Variant ) As [CustomTable](../CustomTable/CustomTable.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ConfigurationFileName | String | Input String that specifies the full file name of the configuration file to create the configuration table from. The file can be an iPart, an iAssembly, or a Presentation file which contains views of an iPart or an iAssembly. |
| PlacementPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that defines the placement point of the table on the sheet. |
| Title | String | Optional input String that specifies the title (or the header) of the table. |
| Columns | Variant | Optional input array of Strings that specifies the columns of the configuration table. The strings specified must be the headings of the columns from the iPart or the iAssembly (obtained using iPartTableColumn.Heading or iAssemblyTableColumn.Heading properties). If not specified, only the 'Member' column is used to create the table.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a Configuration Table](../../sample-programs/CustomTables_AddConfigurationTable_Sample.md) | This sample demonstrates the creation of a configuration (iPart/iAssembly) table in a drawing from a factory document. |

## Version

Introduced in version 2009
