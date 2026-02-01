# PartsList Object

## Description

The PartsList object represents a parts list in a drawing sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CopyTo](../PartsList/PartsList_CopyTo.md) | Method that copies the parts list to another sheet. |
| [Delete](../PartsList/PartsList_Delete.md) | Method that deletes this PartsList. |
| [Export](../PartsList/PartsList_Export.md) | Method that saves the parts list to an external file. |
| [GetReferenceKey](../PartsList/PartsList_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [Renumber](../PartsList/PartsList_Renumber.md) | Method that renumbers all rows in the parts list. |
| [SaveItemOverridesToBOM](../PartsList/PartsList_SaveItemOverridesToBOM.md) | Saves any overrides to the item values in the balloon to the model BOM. |
| [Sort](../PartsList/PartsList_Sort.md) | Method that changes the sort order of items in the parts list. |
| [Sort2](../PartsList/PartsList_Sort2.md) | Changes the sort order of items in the parts list. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PartsList/PartsList_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../PartsList/PartsList_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ColumnHeaderTextStyle](../PartsList/PartsList_ColumnHeaderTextStyle.md) | Gets and sets the text style used for the column titles (headers). |
| [DataTextStyle](../PartsList/PartsList_DataTextStyle.md) | Gets and sets the text style used for the contents of the parts list. |
| [FilterSettings](../PartsList/PartsList_FilterSettings.md) | Read-only property that returns the filter settings for the parts list. |
| [HeadingPlacement](../PartsList/PartsList_HeadingPlacement.md) | Gets and sets the placement position of the table heading. |
| [HideZeroQuantityRows](../PartsList/PartsList_HideZeroQuantityRows.md) | Gets and sets whether to hide rows of zero quantity. |
| [Layer](../PartsList/PartsList_Layer.md) | Gets and sets the layer used by the parts list. |
| [Level](../PartsList/PartsList_Level.md) | Property that returns the type of numbering for the parts list. Possible values are kFirstLevelComponents and kPartsOnly. |
| [MaximumRows](../PartsList/PartsList_MaximumRows.md) | Gets and sets the maximum number of rows per section. |
| [MembersToInclude](../PartsList/PartsList_MembersToInclude.md) | Gets and sets the names of the iPart/iAssembly members to include as columns in the parts list. |
| [NumberingScheme](../PartsList/PartsList_NumberingScheme.md) | Property that returns the numbering scheme used for a 'parts only' parts list. The property returns an error if this is not a 'parts only' parts list. Possible return values are kNumericNumbering, kLowercaseAlphaNumbering and kUppercaseAlphaNumbering. |
| [NumberOfSections](../PartsList/PartsList_NumberOfSections.md) | Gets and sets the number of columns to wrap. |
| [Parent](../PartsList/PartsList_Parent.md) | Property that gets the parent object from whom this object can logically be reached. |
| [PartsListColumns](../PartsList/PartsList_PartsListColumns.md) | Gets the PartsListColumns collection object for this parts list table. |
| [PartsListRows](../PartsList/PartsList_PartsListRows.md) | Gets the PartsListRows collection object for this parts list table. |
| [Position](../PartsList/PartsList_Position.md) | Gets and sets the origin position of the table. |
| [RangeBox](../PartsList/PartsList_RangeBox.md) | Property that returns a Box2D object which contains the lower-left and upper-right corners of a rectangle that is guaranteed to enclose this object. |
| [ReferencedDocumentDescriptor](../PartsList/PartsList_ReferencedDocumentDescriptor.md) | Property that gets the document referenced by this parts list. |
| [Rotation](../PartsList/PartsList_Rotation.md) | Gets and sets the absolute rotation angle of the parts list in radians. |
| [RowGap](../PartsList/PartsList_RowGap.md) | Property that returns the row gap. This value is obtained from the parts list style. |
| [RowLineSpacing](../PartsList/PartsList_RowLineSpacing.md) | Gets and sets the line spacing of the rows. |
| [ShowTitle](../PartsList/PartsList_ShowTitle.md) | Gets and sets whether the title is shown or not. |
| [Style](../PartsList/PartsList_Style.md) | Gets and sets the associated PartsListStyle object. |
| [TableDirection](../PartsList/PartsList_TableDirection.md) | Gets and sets the vertical direction of the table. |
| [Title](../PartsList/PartsList_Title.md) | Gets and sets the title of the parts list. |
| [TitleTextStyle](../PartsList/PartsList_TitleTextStyle.md) | Gets and sets the text style used for the title of the parts list. |
| [Type](../PartsList/PartsList_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WrapAutomatically](../PartsList/PartsList_WrapAutomatically.md) | Gets and sets whether to split the table equally. |
| [WrapLeft](../PartsList/PartsList_WrapLeft.md) | Gets whether the parts list wraps to the left. |

## Accessed From

[PartsList.CopyTo](../PartsList/PartsList_CopyTo.md), [PartsListCell.Parent](../PartsListCell/PartsListCell_Parent.md), [PartsListColumn.Parent](../PartsListColumn/PartsListColumn_Parent.md), [PartsListRow.Parent](../PartsListRow/PartsListRow_Parent.md), [PartsLists.Add](../PartsLists/PartsLists_Add.md), [PartsLists.Item](../PartsLists/PartsLists_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creating a parts list](../../sample-programs/PartsLists_Add_Sample.md) | This sample demonstrates the creation of a parts list. The parts list is placed at the top right corner of the border if one exists, else it is placed at the top right corner of the sheet. |
| [Parts List Edit](../../sample-programs/PartsLists_Edit_Sample.md) | This sample illustrates editing the contents of the parts list. |
| [Parts List Query](../../sample-programs/PartsLists_Query_Sample.md) | This sample illustrates querying the contents of the parts list. |

## Version

Introduced in version 5.3
