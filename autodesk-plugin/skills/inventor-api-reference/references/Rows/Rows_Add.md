# Rows.Add Method

Parent Object: [Rows](../Rows/Rows.md)

## Description

Method that creates a new Row. The new created Row is returned.

## Syntax

Rows.**Add**( [***TargetIndex***] As Long, [***InsertBefore***] As Boolean, [***Contents***] As Variant, [***Height***] As Variant ) As [Row](../Row/Row.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetIndex | Long | Optional input Long that specifies the existing row next to which the new row will be inserted. The valid range of values is 0 to the number of existing rows in the table. A value of 0 will put the row at the end. If not specified, a default value of 0 is used, indicating that the row will be added at the end. |
| InsertBefore | Boolean | Optional input Boolean indicating if the row should be inserted before or after the target index. If not specified, a default value of True is used. This argument is ignored if the value of TargetIndex is 0.   This is an optional argument whose default value is True. |
| Contents | Variant | Optional input array of Strings that specifies the contents of the new row. The number of strings should be equal to the number of columns in the table, else an error will occur.   This is an optional argument whose default value is null. |
| Height | Variant | Optional input Double that specifies the height of the row. If not specified, a default value is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |