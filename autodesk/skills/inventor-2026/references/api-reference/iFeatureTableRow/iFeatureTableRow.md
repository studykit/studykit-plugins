# iFeatureTableRow Object

## Description

The iFeatureTableRow object represents a single row of a table associated with a table driven iFeature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../iFeatureTableRow/iFeatureTableRow_Copy.md) | Method that creates a new row with all cell values equal to the original row with the exception of columns whose values must be unique for each row. These are automatically modified to be unique using the same behavior that you see when inserting a new row in the user-interface. |
| [Delete](../iFeatureTableRow/iFeatureTableRow_Delete.md) | Method that deletes the row from the table. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iFeatureTableRow/iFeatureTableRow_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../iFeatureTableRow/iFeatureTableRow_Count.md) | Property that specifies the number of columns in the row. |
| [Index](../iFeatureTableRow/iFeatureTableRow_Index.md) | Property that returns the index of this row within the iFeatureTableRows collection where the first row has an index of 1. |
| [Item](../iFeatureTableRow/iFeatureTableRow_Item.md) | Method that returns the specified iFeatureTableCell object from the row. |
| [MemberName](../iFeatureTableRow/iFeatureTableRow_MemberName.md) | Property that returns the name that identifies this row. |
| [Parent](../iFeatureTableRow/iFeatureTableRow_Parent.md) | Property that returns the parent iFeatureTable. |
| [Type](../iFeatureTableRow/iFeatureTableRow_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[iFeatureDefinition.ActiveTableRow](../iFeatureDefinition/iFeatureDefinition_ActiveTableRow.md), [iFeatureTable.DefaultRow](../iFeatureTable/iFeatureTable_DefaultRow.md), [iFeatureTableCell.Row](../iFeatureTableCell/iFeatureTableCell_Row.md), [iFeatureTableRow.Copy](../iFeatureTableRow/iFeatureTableRow_Copy.md), [iFeatureTableRows.Item](../iFeatureTableRows/iFeatureTableRows_Item.md)

## Version

Introduced in version 2009
