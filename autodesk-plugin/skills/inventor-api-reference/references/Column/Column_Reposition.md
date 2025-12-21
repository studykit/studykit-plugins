# Column.Reposition Method

Parent Object: [Column](../Column/Column.md)

## Description

Method that repositions the column within the table.

## Syntax

Column.**Reposition**( [***TargetIndex***] As Long, [***InsertBefore***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetIndex | Long | Optional input Long that specifies the existing column next to which the column will be inserted. The valid range of values is 0 to the number of existing columns in the table. The position remains unchanged if the index of the column being moved is specified. A value of 0 will put the column at the end. If not specified, a default value of 0 is used, indicating that the column will be moved to the end. |
| InsertBefore | Boolean | Optional input Boolean indicating if the column should be inserted before or after the target index. If not specified, a default value of True is used indicating that the column will be inserted before the target index. This argument is ignored if the value of TargetIndex is 0.   This is an optional argument whose default value is True. |

## Version

Introduced in version 2009
