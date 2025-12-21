# iFeatureTableColumn Object

## Description

The iFeatureTableColumn object represents a single column of a table associated with a table driven iFeature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../iFeatureTableColumn/iFeatureTableColumn_Delete.md) | Method that deletes the column from the table. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iFeatureTableColumn/iFeatureTableColumn_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../iFeatureTableColumn/iFeatureTableColumn_Count.md) | Property that specifies the number of rows in the column. |
| [CustomColumn](../iFeatureTableColumn/iFeatureTableColumn_CustomColumn.md) | Gets and sets whether this is a custom parameter column. |
| [CustomIncrement](../iFeatureTableColumn/iFeatureTableColumn_CustomIncrement.md) | Gets and sets the increment value for custom parameter column. |
| [CustomRangeMaximum](../iFeatureTableColumn/iFeatureTableColumn_CustomRangeMaximum.md) | Gets and sets the maximum value for a custom parameter column. |
| [CustomRangeMinimum](../iFeatureTableColumn/iFeatureTableColumn_CustomRangeMinimum.md) | Gets and sets the minimum value for a custom parameter column. |
| [DisplayHeading](../iFeatureTableColumn/iFeatureTableColumn_DisplayHeading.md) | Property that returns the heading of the column as seen in the iFeature author command. |
| [FormattedHeading](../iFeatureTableColumn/iFeatureTableColumn_FormattedHeading.md) | Property that returns the heading of the column in XML format. |
| [Heading](../iFeatureTableColumn/iFeatureTableColumn_Heading.md) | Property that returns the heading of the column in XML format. |
| [Index](../iFeatureTableColumn/iFeatureTableColumn_Index.md) | Property that returns the index of this column within the iFeatureTableColumns collection where the first column has an index of 1. |
| [Item](../iFeatureTableColumn/iFeatureTableColumn_Item.md) | Method that returns the specified iFeatureTableCell object from the row. |
| [Key](../iFeatureTableColumn/iFeatureTableColumn_Key.md) | Read-write property that gets and sets the key order for the column. |
| [Parent](../iFeatureTableColumn/iFeatureTableColumn_Parent.md) | Property that returns the parent iFeatureTable. |
| [Type](../iFeatureTableColumn/iFeatureTableColumn_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[iFeatureTableCell.Column](../iFeatureTableCell/iFeatureTableCell_Column.md), [iFeatureTableColumns.Item](../iFeatureTableColumns/iFeatureTableColumns_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Place table driven iFeature](../../sample-programs/iFeatureTable_Sample.md) | This program demonstrates the placement of a table driven iFeature in a part. |
| [Changing row of table driven iFeature](../../sample-programs/iFeatureTable_iFeatureTableColumns_Sample.md) | This program demonstrates the edit of a table driven iFeature to change which row of the table is being used to drive the iFeature. |

## Version

Introduced in version 2009
