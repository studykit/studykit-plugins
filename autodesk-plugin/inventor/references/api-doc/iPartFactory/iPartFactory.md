# iPartFactory Object

## Description

The iPartFactory object provides access to the iPart table and provides methods to create additional iPart members ( objects).

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CreateCustomMember](../iPartFactory/iPartFactory_CreateCustomMember.md) | Method that creates an iPart member for a custom factory using the parameter values in a row. The created iPartMember is returned. |
| [CreateMember](../iPartFactory/iPartFactory_CreateMember.md) | Method that creates an iPart member using the parameter values in a row. The created iPartMember is returned. |
| [Delete](../iPartFactory/iPartFactory_Delete.md) | Method that converts an iPart factory to a regular part. When an iPart factory is converted to a regular part, all of the iPart members created from the factory become sick. |
| [Export](../iPartFactory/iPartFactory_Export.md) | Exports the iPartFactory to an external file. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iPartFactory/iPartFactory_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [CustomFactory](../iPartFactory/iPartFactory_CustomFactory.md) | Property that specifies whether this iPartFactory object represents a custom factory or a standard factory. This property is True in the case where it represents a custom factory. |
| [DefaultRow](../iPartFactory/iPartFactory_DefaultRow.md) | Gets and sets the default row for this iPart factory. |
| [DisplayStyleColumn](../iPartFactory/iPartFactory_DisplayStyleColumn.md) | Gets and sets the column to use as the display (render) style column. |
| [ExcelWorkSheet](../iPartFactory/iPartFactory_ExcelWorkSheet.md) | Property that returns the Excel spreadsheet that represents the iPart table. |
| [FactoryOptions](../iPartFactory/iPartFactory_FactoryOptions.md) | Property that gets the options for the factory. |
| [FileNameColumn](../iPartFactory/iPartFactory_FileNameColumn.md) | Gets and sets the column to use as the file name column. |
| [MaterialColumn](../iPartFactory/iPartFactory_MaterialColumn.md) | Gets and sets the column to use as the material column. |
| [MemberCacheDir](../iPartFactory/iPartFactory_MemberCacheDir.md) | Property that returns the directory location for the newly created iPart members. |
| [MemberEditScope](../iPartFactory/iPartFactory_MemberEditScope.md) | Gets and sets whether the edits to a member should affect just the active member or all members within the factory. |
| [Parent](../iPartFactory/iPartFactory_Parent.md) | Property that returns the parent PartDocument of the factory. |
| [TableColumns](../iPartFactory/iPartFactory_TableColumns.md) | Property that returns the iPartTableColumns collection object. |
| [TableRows](../iPartFactory/iPartFactory_TableRows.md) | Property that returns the iPartTableRows collection object. |
| [Type](../iPartFactory/iPartFactory_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[iPartMember.ParentFactory](../iPartMember/iPartMember_ParentFactory.md), [iPartTableCell.Parent](../iPartTableCell/iPartTableCell_Parent.md), [iPartTableColumn.Parent](../iPartTableColumn/iPartTableColumn_Parent.md), [iPartTableRow.Parent](../iPartTableRow/iPartTableRow_Parent.md), [PartComponentDefinition.CreateFactory](../PartComponentDefinition/PartComponentDefinition_CreateFactory.md), [PartComponentDefinition.iPartFactory](../PartComponentDefinition/PartComponentDefinition_iPartFactory.md), [SheetMetalComponentDefinition.CreateFactory](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_CreateFactory.md), [SheetMetalComponentDefinition.iPartFactory](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_iPartFactory.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iPart occurrences to an assembly](../../sample-programs/AddiPartMember_Sample.md) | This sample demonstrates adding iPart occurrences to an assembly. |
| [Create a Configuration Table](../../sample-programs/CustomTables_AddConfigurationTable_Sample.md) | This sample demonstrates the creation of a configuration (iPart/iAssembly) table in a drawing from a factory document. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |