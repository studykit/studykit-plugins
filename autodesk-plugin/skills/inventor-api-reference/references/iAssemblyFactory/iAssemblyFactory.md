# iAssemblyFactory Object

## Description

The iAssemblyFactory object provides access to the iAssembly table and provides methods to create iAssembly members.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CreateMember](../iAssemblyFactory/iAssemblyFactory_CreateMember.md) | Method that creates an iAssembly member using the parameter values in a row. The created iAssemblyMember is returned. If the member already exists, the member is updated and the iAssemblyMember object is returned. |
| [Delete](../iAssemblyFactory/iAssemblyFactory_Delete.md) | Method that converts the iAssembly factory to a regular assembly. When an iAssembly factory is converted to a regular assembly, all of the iAssembly members created from the factory become sick. |
| [Export](../iAssemblyFactory/iAssemblyFactory_Export.md) | Method that exports the iAssemblyFactory to an external file. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iAssemblyFactory/iAssemblyFactory_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DefaultRow](../iAssemblyFactory/iAssemblyFactory_DefaultRow.md) | Read-write property that gets and sets the default row for this iAssemblyFactory. |
| [ExcelWorkSheet](../iAssemblyFactory/iAssemblyFactory_ExcelWorkSheet.md) | Property that returns the excel spreadsheet that represents the iAssembly table. |
| [FactoryOptions](../iAssemblyFactory/iAssemblyFactory_FactoryOptions.md) | Property that gets the options for the factory. |
| [FileNameColumn](../iAssemblyFactory/iAssemblyFactory_FileNameColumn.md) | Read-write property that gets and sets the column to use as the file name column. |
| [MemberCacheDir](../iAssemblyFactory/iAssemblyFactory_MemberCacheDir.md) | Property that returns the directory location for the newly created iAssembly members. |
| [MemberEditScope](../iAssemblyFactory/iAssemblyFactory_MemberEditScope.md) | Read-write property that gets and sets whether the edits to a member should affect just the active member or all members within the factory. |
| [Parent](../iAssemblyFactory/iAssemblyFactory_Parent.md) | Property that returns the parent AssemblyComponentDefinition of the factory. |
| [TableColumns](../iAssemblyFactory/iAssemblyFactory_TableColumns.md) | Property that returns the iAssemblyTableColumns collection object. |
| [TableRows](../iAssemblyFactory/iAssemblyFactory_TableRows.md) | Property that returns the iAssemblyTableRows collection object. |
| [Type](../iAssemblyFactory/iAssemblyFactory_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.CreateFactory](../AssemblyComponentDefinition/AssemblyComponentDefinition_CreateFactory.md), [AssemblyComponentDefinition.iAssemblyFactory](../AssemblyComponentDefinition/AssemblyComponentDefinition_iAssemblyFactory.md), [iAssemblyMember.ParentFactory](../iAssemblyMember/iAssemblyMember_ParentFactory.md), [iAssemblyTableCell.Parent](../iAssemblyTableCell/iAssemblyTableCell_Parent.md), [iAssemblyTableColumn.Parent](../iAssemblyTableColumn/iAssemblyTableColumn_Parent.md), [iAssemblyTableRow.Parent](../iAssemblyTableRow/iAssemblyTableRow_Parent.md), [WeldmentComponentDefinition.CreateFactory](../WeldmentComponentDefinition/WeldmentComponentDefinition_CreateFactory.md), [WeldmentComponentDefinition.iAssemblyFactory](../WeldmentComponentDefinition/WeldmentComponentDefinition_iAssemblyFactory.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iAssembly occurrences](../../sample-programs/AddiAssemblyMember_Sample.md) | This sample demonstrates adding iAssembly occurrences to an assembly. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |