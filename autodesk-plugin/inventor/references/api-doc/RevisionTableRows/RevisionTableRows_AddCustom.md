# RevisionTableRows.AddCustom Method

Parent Object: [RevisionTableRows](../RevisionTableRows/RevisionTableRows.md)

## Description

Creates a new custom RevisionTableRow.

## Syntax

RevisionTableRows.**AddCustom**( [***TargetIndex***] As Long, [***InsertBefore***] As Boolean ) As [RevisionTableRow](../RevisionTableRow/RevisionTableRow.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetIndex | Long | Optional input Long that specifies the existing row next to which the new row will be inserted. The valid range of values is 0 to the number of existing rows in the table. A value of 0 will put the row at the end. If not specified, a default value of 0 is used, indicating that the row will be added at the end. |
| InsertBefore | Boolean | Optional input Boolean indicating if the row should be inserted before or after the target index. If not specified, a default value of True is used. This argument is ignored if the value of TargetIndex is 0.   This is an optional argument whose default value is True. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |