# PartsListRows.Add Method

Parent Object: [PartsListRows](../PartsListRows/PartsListRows.md)

## Description

Method that creates a custom PartsListRow. The newly created PartsListRow is returned.

## Syntax

PartsListRows.**Add**( [***TargetIndex***] As Long, [***InsertBefore***] As Boolean ) As [PartsListRow](../PartsListRow/PartsListRow.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetIndex | Long | Optional input Long that specifies the existing row next to which the new row will be inserted. The valid range of values is 0 to the number of existing rows in the table. A value of 0 will put the row at the end. If not specified, a default value of 0 is used, indicating that the row will be added at the end. |
| InsertBefore | Boolean | Optional input Boolean indicating if the row should be inserted before or after the target index. If not specified, a default value of True is used. This argument is ignored if the value of TargetIndex is 0.   This is an optional argument whose default value is True. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |