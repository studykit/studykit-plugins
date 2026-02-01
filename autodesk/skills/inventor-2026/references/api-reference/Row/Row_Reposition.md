# Row.Reposition Method

Parent Object: [Row](../Row/Row.md)

## Description

Method that repositions the row within the table.

## Syntax

Row.**Reposition**( [***TargetIndex***] As Long, [***InsertBefore***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetIndex | Long | Optional input Long that specifies the existing row next to which the row will be inserted. The valid range of values is 0 to the number of existing rows in the table. The position remains unchanged if the index of the row being moved is specified. A value of 0 will put the row at the end. If not specified, a default value of 0 is used, indicating that the row will be moved to the end. |
| InsertBefore | Boolean | Optional input Boolean indicating if the row should be inserted before or after the target index. If not specified, a default value of True is used indicating that the row will be inserted before the target index. This argument is ignored if the value of TargetIndex is 0.   This is an optional argument whose default value is True. |

## Version

Introduced in version 2009
