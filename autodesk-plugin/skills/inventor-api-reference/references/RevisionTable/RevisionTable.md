# RevisionTable Object

## Description

This object represent a revision table.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CopyTo](../RevisionTable/RevisionTable_CopyTo.md) | Copies the revision table to another sheet, sheet scope revision tables may not be copied. |
| [Delete](../RevisionTable/RevisionTable_Delete.md) | Method that deletes the RevisionTable. |
| [Export](../RevisionTable/RevisionTable_Export.md) | Saves the revision table to an external file. |
| [GetReferenceKey](../RevisionTable/RevisionTable_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [Sort](../RevisionTable/RevisionTable_Sort.md) | Changes the sort order of rows in the revision table. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RevisionTable/RevisionTable_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../RevisionTable/RevisionTable_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ColumnHeaderTextStyle](../RevisionTable/RevisionTable_ColumnHeaderTextStyle.md) | Gets and sets the text style used for the column titles (headers). |
| [DataTextStyle](../RevisionTable/RevisionTable_DataTextStyle.md) | Gets and sets the text style used for the contents of the revision table. |
| [HeadingGap](../RevisionTable/RevisionTable_HeadingGap.md) | Gets the heading gap. |
| [HeadingPlacement](../RevisionTable/RevisionTable_HeadingPlacement.md) | Gets and sets the location of the heading. |
| [IsSheetScope](../RevisionTable/RevisionTable_IsSheetScope.md) | Gets whether the scope of the revision table is the entire drawing or the parent sheet. |
| [Layer](../RevisionTable/RevisionTable_Layer.md) | Gets and sets the layer used by the revision table. |
| [MaximumRows](../RevisionTable/RevisionTable_MaximumRows.md) | Gets and sets the maximum number of rows per section. |
| [NumberOfSections](../RevisionTable/RevisionTable_NumberOfSections.md) | Gets and sets the number of columns to wrap. |
| [Parent](../RevisionTable/RevisionTable_Parent.md) | Property that returns the parent object of this RevisionTable. |
| [Position](../RevisionTable/RevisionTable_Position.md) | Gets/Sets the position of the RevisionTable on the sheet. |
| [RangeBox](../RevisionTable/RevisionTable_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [RevisionTableColumns](../RevisionTable/RevisionTable_RevisionTableColumns.md) | Property that returns the RevisionTableColumns collection object. |
| [RevisionTableRows](../RevisionTable/RevisionTable_RevisionTableRows.md) | Property that returns the RevisionTableRows collection object. |
| [Rotation](../RevisionTable/RevisionTable_Rotation.md) | Gets and sets the absolute rotation angle of the revision table in radians. |
| [RowGap](../RevisionTable/RevisionTable_RowGap.md) | Gets the row gap. |
| [RowLineSpacing](../RevisionTable/RevisionTable_RowLineSpacing.md) | Gets and sets the spacing between the rows. |
| [ShowTitle](../RevisionTable/RevisionTable_ShowTitle.md) | Gets and sets whether to show the title of the revision table. |
| [Style](../RevisionTable/RevisionTable_Style.md) | Gets and sets the style associated with this object. |
| [TableDirection](../RevisionTable/RevisionTable_TableDirection.md) | Gets and sets the direction of the table. |
| [Title](../RevisionTable/RevisionTable_Title.md) | Gets/Sets the title of the RevisionTable. |
| [TitleTextStyle](../RevisionTable/RevisionTable_TitleTextStyle.md) | Gets and sets the text style used for the title of the revision table. |
| [Type](../RevisionTable/RevisionTable_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UpdatePropertyToRevisionNumber](../RevisionTable/RevisionTable_UpdatePropertyToRevisionNumber.md) | Gets and sets whether any edits made to the revision number cell in the active row are written back to either the Revision Number iProperty or sheet revision property (depending on the revision table scope). |
| [WrapAutomatically](../RevisionTable/RevisionTable_WrapAutomatically.md) | Gets and sets whether to split the table equally. |
| [WrapLeft](../RevisionTable/RevisionTable_WrapLeft.md) | Gets and sets whether the sections of the revision table are moved to the left or right when the number of rows increase. |

## Accessed From

[RevisionTable.CopyTo](../RevisionTable/RevisionTable_CopyTo.md), [RevisionTableCell.Parent](../RevisionTableCell/RevisionTableCell_Parent.md), [RevisionTableColumn.Parent](../RevisionTableColumn/RevisionTableColumn_Parent.md), [RevisionTableRow.Parent](../RevisionTableRow/RevisionTableRow_Parent.md), [RevisionTables.Add](../RevisionTables/RevisionTables_Add.md), [RevisionTables.Add2](../RevisionTables/RevisionTables_Add2.md), [RevisionTables.Item](../RevisionTables/RevisionTables_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Query revision table](../../sample-programs/RevisionTable_Sample.md) | This sample illustrates querying the contents of the revision table. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |