# iFeatureTable Object

## Description

The iFeatureTable object represents the table associated with a table driven iFeature. This object provides access to the contents of the table and provides information about the default and active rows.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../iFeatureTable/iFeatureTable_Delete.md) | Method that deletes the iFeatureTable. This converts a table driven iFeature into a standard iFeature. |
| [Export](../iFeatureTable/iFeatureTable_Export.md) | Exports the iFeatureTable to an external file. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iFeatureTable/iFeatureTable_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DefaultRow](../iFeatureTable/iFeatureTable_DefaultRow.md) | Gets and sets the default row. |
| [ExcelWorkSheet](../iFeatureTable/iFeatureTable_ExcelWorkSheet.md) | Property that returns the Excel WorkSheet object representing the iFeature table. After making changes to the Excel sheet, save and close the parent WorkBook object of the sheet in order for Inventor to absorb the changes. |
| [iFeatureTableColumns](../iFeatureTable/iFeatureTable_iFeatureTableColumns.md) | Property returning the collection of columns in the table. |
| [iFeatureTableRows](../iFeatureTable/iFeatureTable_iFeatureTableRows.md) | Property returning the collection of rows in the table. |
| [Parent](../iFeatureTable/iFeatureTable_Parent.md) | Property returning the parent object. |
| [Type](../iFeatureTable/iFeatureTable_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[iFeatureDefinition.iFeatureTable](../iFeatureDefinition/iFeatureDefinition_iFeatureTable.md), [iFeatureTableCell.Parent](../iFeatureTableCell/iFeatureTableCell_Parent.md), [iFeatureTableColumn.Parent](../iFeatureTableColumn/iFeatureTableColumn_Parent.md), [iFeatureTableRow.Parent](../iFeatureTableRow/iFeatureTableRow_Parent.md)

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |