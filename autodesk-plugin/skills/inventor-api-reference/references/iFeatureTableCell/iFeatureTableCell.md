# iFeatureTableCell Object

## Description

The iFeatureTableCell object represents a single cell within a table associated with a table driven iFeature.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iFeatureTableCell/iFeatureTableCell_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Column](../iFeatureTableCell/iFeatureTableCell_Column.md) | Property that returns the column this cell is within. |
| [CustomCell](../iFeatureTableCell/iFeatureTableCell_CustomCell.md) | Gets and sets whether this is a custom parameter cell. |
| [CustomIncrement](../iFeatureTableCell/iFeatureTableCell_CustomIncrement.md) | Gets and sets the increment value for custom parameter cell. |
| [CustomRangeMaximum](../iFeatureTableCell/iFeatureTableCell_CustomRangeMaximum.md) | Gets and sets the maximum value for a custom parameter cell. |
| [CustomRangeMinimum](../iFeatureTableCell/iFeatureTableCell_CustomRangeMinimum.md) | Gets and sets the minimum value for a custom parameter cell. |
| [HasFormula](../iFeatureTableCell/iFeatureTableCell_HasFormula.md) | Gets whether a formula (equation) was input into this cell via Excel. |
| [IsValid](../iFeatureTableCell/iFeatureTableCell_IsValid.md) | Gets whether the contents of this cell are valid. |
| [Parent](../iFeatureTableCell/iFeatureTableCell_Parent.md) | Property that returns the parent iFeatureTable. |
| [Row](../iFeatureTableCell/iFeatureTableCell_Row.md) | Property that returns the row this cell is within. |
| [Type](../iFeatureTableCell/iFeatureTableCell_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Value](../iFeatureTableCell/iFeatureTableCell_Value.md) | Gets and sets the value of the cell. |

## Accessed From

[iFeatureTableColumn.Item](../iFeatureTableColumn/iFeatureTableColumn_Item.md), [iFeatureTableRow.Item](../iFeatureTableRow/iFeatureTableRow_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Place table driven iFeature](../../sample-programs/iFeatureTable_Sample.md) | This program demonstrates the placement of a table driven iFeature in a part. |
| [Changing row of table driven iFeature](../../sample-programs/iFeatureTable_iFeatureTableColumns_Sample.md) | This program demonstrates the edit of a table driven iFeature to change which row of the table is being used to drive the iFeature. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |