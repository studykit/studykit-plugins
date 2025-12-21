# HoleTableColumns.Add Method

Parent Object: [HoleTableColumns](../HoleTableColumns/HoleTableColumns.md)

## Description

Method that creates a new HoleTableColumn based on a property. The newly created HoleTableColumn is returned.

## Syntax

HoleTableColumns.**Add**( ***PropertyType*** As [HolePropertyEnum](../HolePropertyEnum.md), [***CustomPropertyName***] As String, [***TargetIndex***] As Long, [***InsertBefore***] As Boolean ) As [HoleTableColumn](../HoleTableColumn/HoleTableColumn.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PropertyType | [HolePropertyEnum](../HolePropertyEnum.md) | Input HolePropertyEnum that specifies the property type to associate with the column. If kCustomHoleProperty is specified, the CustomPropertyName argument is required. |
| CustomPropertyName | String | Optional input String that specifies the name of the custom property to associate with the column. This argument must be specified if the PropertyType is specified to be kCustomHoleProperty, else the method returns an error. |
| TargetIndex | Long | Optional input Long that specifies the existing column next to which the new column will be inserted. The valid range of values is 0 to the number of existing columns in the table. A value of 0 will put the row at the end. If not specified, a default value of 0 is used, indicating that the column will be added at the end.   This is an optional argument whose default value is 0. |
| InsertBefore | Boolean | Optional input Boolean indicating if the column should be inserted before or after the target index. If not specified, a default value of True is used. This argument is ignored if the value of TargetIndex is 0.   This is an optional argument whose default value is True. |

## Version

Introduced in version 2009
