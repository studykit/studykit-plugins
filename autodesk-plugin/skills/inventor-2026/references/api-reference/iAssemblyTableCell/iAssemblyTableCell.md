# iAssemblyTableCell Object

## Description

The iAssemblyTableCell object represents an individual cell in the iAssembly factory table.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iAssemblyTableCell/iAssemblyTableCell_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Column](../iAssemblyTableCell/iAssemblyTableCell_Column.md) | Property that returns the index of this cell within the parent iAssemblyTableColumn. |
| [HasFormula](../iAssemblyTableCell/iAssemblyTableCell_HasFormula.md) | Property that returns whether a formula (equation) was input into this cell via Excel. Such cells show with a red background in the user interface and are not editable. |
| [IsValid](../iAssemblyTableCell/iAssemblyTableCell_IsValid.md) | Property that returns whether the contents of this cell are valid. Invalid cells show with a yellow background in the user interface. |
| [Parent](../iAssemblyTableCell/iAssemblyTableCell_Parent.md) | Property that returns the parent iAssemblyFactory object. |
| [Row](../iAssemblyTableCell/iAssemblyTableCell_Row.md) | Property that returns the index of this cell within the parent iAssemblyTableRow. |
| [Type](../iAssemblyTableCell/iAssemblyTableCell_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Value](../iAssemblyTableCell/iAssemblyTableCell_Value.md) | Read-write property that gets and sets the value of the cell. |

## Accessed From

[iAssemblyTableColumn.Item](../iAssemblyTableColumn/iAssemblyTableColumn_Item.md), [iAssemblyTableRow.Item](../iAssemblyTableRow/iAssemblyTableRow_Item.md)

## Version

Introduced in version 11
