# Columns.Add Method

Parent Object: [Columns](../Columns/Columns.md)

## Description

Method that creates a new Column. The new created Column is returned.

## Syntax

Columns.**Add**( ***Title*** As String, [***TargetIndex***] As Long, [***InsertBefore***] As Boolean, [***Width***] As Variant ) As [Column](../Column/Column.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Title | String | Input String that specifies the title for the column. |
| TargetIndex | Long | Optional input Long that specifies the existing column next to which the new column will be inserted. The valid range of values is 0 to the number of existing columns in the table. A value of 0 will put the row at the end. If not specified, a default value of 0 is used, indicating that the column will be added at the end. |
| InsertBefore | Boolean | Optional input Boolean indicating if the column should be inserted before or after the target index. If not specified, a default value of True is used. This argument is ignored if the value of TargetIndex is 0.   This is an optional argument whose default value is True. |
| Width | Variant | Optional input Double that specifies the width of the column. If not specified, a default value is used.   This is an optional argument whose default value is null. |

## Version

Introduced in version 9
