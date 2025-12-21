# Sheet.Border Property

Parent Object: [Sheet](../Sheet/Sheet.md)

## Description

Property that returns the Border or DefaultBorder object associated with the sheet. This property will return Nothing in the case where the sheet doesn't have a border.

## Syntax

Sheet.**Border**() As [Border](../Border/Border.md)

## Property Value

This is a read only property whose value is a [Border](../Border/Border.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Border Create and Insert](../../sample-programs/DrawingDocument_BorderDefinitions_Sample.md) | This sample illustrates creating a new border definition object and using it for a sheet. |
| [Creating hole tables](../../sample-programs/HoleTables_Add_Sample.md) | This sample demonstrates the creation of hole tables in a drawing. |
| [Creating a parts list](../../sample-programs/PartsLists_Add_Sample.md) | This sample demonstrates the creation of a parts list. The parts list is placed at the top right corner of the border if one exists, else it is placed at the top right corner of the sheet. |
| [Border Insert](../../sample-programs/Sheet_AddDefaultBorder_Sample.md) | This sample illustrates inserting a default border. |
| [Border Insert Default](../../sample-programs/Sheet_AddDefaultBorder2_Sample.md) | This sample illustrates inserting a default border using the default values. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |