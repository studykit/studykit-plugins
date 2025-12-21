# iPartTableCell Object

## Description

The iPartTableCell object represents an individual cell in the iPart factory table.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iPartTableCell/iPartTableCell_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Column](../iPartTableCell/iPartTableCell_Column.md) | Property that returns the index of this cell within the parent iPartTableColumn. |
| [CustomCell](../iPartTableCell/iPartTableCell_CustomCell.md) | Gets and sets whether this is a custom parameter cell. |
| [CustomIncrement](../iPartTableCell/iPartTableCell_CustomIncrement.md) | Gets and sets the increment value for custom parameter cell. |
| [CustomRangeMaximum](../iPartTableCell/iPartTableCell_CustomRangeMaximum.md) | Gets and sets the maximum value for a custom parameter. |
| [CustomRangeMinimum](../iPartTableCell/iPartTableCell_CustomRangeMinimum.md) | Gets and sets the minimum value for a custom parameter. |
| [HasFormula](../iPartTableCell/iPartTableCell_HasFormula.md) | Property that returns whether a formula (equation) was input into this cell via Excel. Such cells show with a red background in the user interface and are not editable. |
| [IsValid](../iPartTableCell/iPartTableCell_IsValid.md) | Property that returns whether the contents of this cell are valid. Invalid cells show with a yellow background in the user interface. |
| [Parent](../iPartTableCell/iPartTableCell_Parent.md) | Property that returns the parent iPartTableRow object. |
| [Row](../iPartTableCell/iPartTableCell_Row.md) | Property that returns the index of this cell within the parent iPartTableRow. |
| [Type](../iPartTableCell/iPartTableCell_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Value](../iPartTableCell/iPartTableCell_Value.md) | Gets and sets the value of the cell. |

## Accessed From

[iPartTableColumn.Item](../iPartTableColumn/iPartTableColumn_Item.md), [iPartTableRow.Item](../iPartTableRow/iPartTableRow_Item.md)

## Version

Introduced in version 6
