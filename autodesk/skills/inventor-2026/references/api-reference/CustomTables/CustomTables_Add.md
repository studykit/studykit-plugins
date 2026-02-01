# CustomTables.Add Method

Parent Object: [CustomTables](../CustomTables/CustomTables.md)

## Description

Method that creates a new CustomTable. The new created CustomTable is returned.

## Syntax

CustomTables.**Add**( ***Title*** As String, ***PlacementPoint*** As [Point2d](../Point2d/Point2d.md), ***NumberOfColumns*** As Long, ***NumberOfRows*** As Long, ***ColumnTitles***() As String, [***Contents***] As Variant, [***ColumnWidths***] As Variant, [***RowHeights***] As Variant, [***MoreInfo***] As Variant ) As [CustomTable](../CustomTable/CustomTable.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Title | String | String that specifies the title (or the header) of the table. |
| PlacementPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that defines the placement point of the table. |
| NumberOfColumns | Long | Input Long that specifies the number of columns in the table. |
| NumberOfRows | Long | Input Long that specifies the number of rows in the table. |
| ColumnTitles | String | Array of Strings that specifies the titles of the columns. The number of strings should be equal to the number of columns, else an error will occur. |
| Contents | Variant | Optional input String array that specifies the contents of the table. The number of Strings must match the number of cells in the table, else an error will occur. This array of String is used to sequentially populate each row of the table. |
| ColumnWidths | Variant | Optional input array of Doubles that specifies the width of the columns. The number of doubles specified must be equal to the number of columns, else an error will occur. If not specified, a default value is used.   This is an optional argument whose default value is null. |
| RowHeights | Variant | Optional input array of Doubles that specifies the height of the rows. The number of doubles specified must be equal to the number of rows, else an error will occur. If not specified, a default value is used.   This is an optional argument whose default value is null. |
| MoreInfo | Variant | Optional input NameValueMap that specifies additional information for the table creation. This argument is currently ignored.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Custom Table - create](../../sample-programs/CustomTables_Sample.md) | This sample demonstrates how to create a custom table. |

## Version

Introduced in version 9
