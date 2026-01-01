# Cell Object

## Description

The Cell object represents an individual cell in the table. A cell is the intersection between a column and a row. See the Custom Tables article in the overviews section for more information.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Cell/Cell_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Column](../Cell/Cell_Column.md) | Returns the index of this cell within the parent Column. |
| [IsMerged](../Cell/Cell_IsMerged.md) | Returns whether this cell is merged or not. |
| [MergedCell](../Cell/Cell_MergedCell.md) | Returns the merged cell that this cell is merged in. |
| [Parent](../Cell/Cell_Parent.md) | Property that returns the parent Table object. |
| [Row](../Cell/Cell_Row.md) | Returns the index of this cell within the parent Row. |
| [Static](../Cell/Cell_Static.md) | Gets and sets whether or not the contents of this cell are static. |
| [Type](../Cell/Cell_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Value](../Cell/Cell_Value.md) | Specifies the value of the cell. |

## Accessed From

[MergedCell.EndCell](../MergedCell/MergedCell_EndCell.md), [MergedCell.StartCell](../MergedCell/MergedCell_StartCell.md), [Row.Item](../Row/Row_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Parts List Edit](../../sample-programs/PartsLists_Edit_Sample.md) | This sample illustrates editing the contents of the parts list. |
| [Parts List Query](../../sample-programs/PartsLists_Query_Sample.md) | This sample illustrates querying the contents of the parts list. |

## Version

Introduced in version 9
