# CustomTable Object

## Description

The CustomTable object allows the creation of user-defined tables with the specified number of rows and columns, headings, content, and so on. See the Custom Tables overview for more information.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddBendTagsToView](../CustomTable/CustomTable_AddBendTagsToView.md) | Method that adds bend tags to drawing view. |
| [AddLink](../CustomTable/CustomTable_AddLink.md) | Method that adds a link to the specified document. If a link to a foreign file type already exists, the link is replaced if the input is also a foreign file. |
| [CopyTo](../CustomTable/CustomTable_CopyTo.md) | Method that copies the table to another sheet, either within the same document or in another document. |
| [Delete](../CustomTable/CustomTable_Delete.md) | Method that deletes the CustomTable. |
| [Export](../CustomTable/CustomTable_Export.md) | Method that saves the custom table to an external file. |
| [GetReferenceKey](../CustomTable/CustomTable_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [MergeCells](../CustomTable/CustomTable_MergeCells.md) | Merges the table cells. |
| [Renumber](../CustomTable/CustomTable_Renumber.md) | Method that renumbers all rows in the table. This method applies only to bend tables and returns an error for all other tables. |
| [Sort](../CustomTable/CustomTable_Sort.md) | Method that sorts the table. |
| [Update](../CustomTable/CustomTable_Update.md) | Method that updates the custom table if it is out of date with respect to its linked files. The method returns a success and returns trivially if no update is required. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CustomTable/CustomTable_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../CustomTable/CustomTable_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BendDirectionReversed](../CustomTable/CustomTable_BendDirectionReversed.md) | Gets and sets whether the bend direction is reversed. |
| [ColumnHeaderTextStyle](../CustomTable/CustomTable_ColumnHeaderTextStyle.md) | Gets and sets the text style used for the column titles (headers). |
| [Columns](../CustomTable/CustomTable_Columns.md) | Property that returns the Columns collection object. |
| [DataTextStyle](../CustomTable/CustomTable_DataTextStyle.md) | Gets and sets the text style used for the contents of the table. |
| [HeadingPlacement](../CustomTable/CustomTable_HeadingPlacement.md) | Gets and sets the placement position of the table heading. |
| [Layer](../CustomTable/CustomTable_Layer.md) | Gets and sets the layer used by the table. |
| [MaximumRows](../CustomTable/CustomTable_MaximumRows.md) | Gets and sets the maximum number of rows per section. |
| [MergedCells](../CustomTable/CustomTable_MergedCells.md) | Returns all MergedCell objects in a table. |
| [NumberOfSections](../CustomTable/CustomTable_NumberOfSections.md) | Gets and sets the number of columns to wrap. |
| [OverrideFormat](../CustomTable/CustomTable_OverrideFormat.md) | Gets and sets the table format. |
| [Parent](../CustomTable/CustomTable_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [Position](../CustomTable/CustomTable_Position.md) | Specifies the position of the table. |
| [RangeBox](../CustomTable/CustomTable_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [ReferencedDocumentDescriptor](../CustomTable/CustomTable_ReferencedDocumentDescriptor.md) | Property that returns either a DocumentDescriptor object (for Inventor references) or a FileDescriptor object (for foreign file references). The property returns Nothing if no links have been specified for the table. |
| [Rotation](../CustomTable/CustomTable_Rotation.md) | Gets and sets the absolute rotation angle of the table in radians. |
| [RowGap](../CustomTable/CustomTable_RowGap.md) | Property that returns the row gap. |
| [RowLineSpacing](../CustomTable/CustomTable_RowLineSpacing.md) | Gets and sets the spacing between the rows. |
| [Rows](../CustomTable/CustomTable_Rows.md) | Property that returns the Rows collection object. |
| [ShowTitle](../CustomTable/CustomTable_ShowTitle.md) | Gets and sets whether to show the title of the table. |
| [Style](../CustomTable/CustomTable_Style.md) | Gets and sets the style associated with this object. |
| [TableDirection](../CustomTable/CustomTable_TableDirection.md) | Gets and sets the vertical direction of the table. |
| [TableSource](../CustomTable/CustomTable_TableSource.md) | Property that returns the source type for this table. |
| [Title](../CustomTable/CustomTable_Title.md) | Specifies the title of the table. |
| [TitleTextStyle](../CustomTable/CustomTable_TitleTextStyle.md) | Gets and sets the text style used for the title of the table. |
| [Type](../CustomTable/CustomTable_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WrapAutomatically](../CustomTable/CustomTable_WrapAutomatically.md) | Gets and sets whether to split the table equally. |
| [WrapLeft](../CustomTable/CustomTable_WrapLeft.md) | Gets and sets whether the sections of the table are moved to the left or right when the number of rows increase. |

## Accessed From

[Cell.Parent](../Cell/Cell_Parent.md), [Column.Parent](../Column/Column_Parent.md), [CustomTable.CopyTo](../CustomTable/CustomTable_CopyTo.md), [CustomTables.Add](../CustomTables/CustomTables_Add.md), [CustomTables.AddBendTableWithOptions](../CustomTables/CustomTables_AddBendTableWithOptions.md), [CustomTables.AddConfigurationTable](../CustomTables/CustomTables_AddConfigurationTable.md), [CustomTables.AddCSVTable](../CustomTables/CustomTables_AddCSVTable.md), [CustomTables.AddExcelTable](../CustomTables/CustomTables_AddExcelTable.md), [CustomTables.Item](../CustomTables/CustomTables_Item.md), [MergedCell.Parent](../MergedCell/MergedCell_Parent.md), [Row.Parent](../Row/Row_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Custom Table - create](../../sample-programs/CustomTables_Sample.md) | This sample demonstrates how to create a custom table. |
| [Create a Bend Table](../../sample-programs/CustomTables_AddBendTable_Sample.md) | This sample demonstrates the creation of a bend table in a drawing from a sheet metal part. |
| [Create a Configuration Table](../../sample-programs/CustomTables_AddConfigurationTable_Sample.md) | This sample demonstrates the creation of a configuration (iPart/iAssembly) table in a drawing from a factory document. |
| [Create a drawing Excel Table](../../sample-programs/CustomTables_AddExcelTable_Sample.md) | This sample demonstrates the creation of a table based on an Excel file in a drawing. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |