# iAssemblyTableColumn Object

## Description

The iAssemblyTableColumn object represents a column in the iAssembly factory table.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../iAssemblyTableColumn/iAssemblyTableColumn_Delete.md) | Deletes this column in the factory. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iAssemblyTableColumn/iAssemblyTableColumn_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../iAssemblyTableColumn/iAssemblyTableColumn_Count.md) | Property that specifies the number of items in the collection. |
| [DisplayHeading](../iAssemblyTableColumn/iAssemblyTableColumn_DisplayHeading.md) | Property that returns the localized heading of the column. |
| [FormattedHeading](../iAssemblyTableColumn/iAssemblyTableColumn_FormattedHeading.md) | Property that returns the heading of the column in XML format. |
| [Heading](../iAssemblyTableColumn/iAssemblyTableColumn_Heading.md) | Property that returns the non-localized heading of the column. |
| [Index](../iAssemblyTableColumn/iAssemblyTableColumn_Index.md) | Property that returns the index of this column within the iAssembly factory table. |
| [Item](../iAssemblyTableColumn/iAssemblyTableColumn_Item.md) | Returns the specified iAssemblyTableCell object from the collection. |
| [Key](../iAssemblyTableColumn/iAssemblyTableColumn_Key.md) | Read-write property that gets and sets the key order for the column. |
| [Parent](../iAssemblyTableColumn/iAssemblyTableColumn_Parent.md) | Property that returns the parent iAssemblyFactory object. |
| [ReferencedDataType](../iAssemblyTableColumn/iAssemblyTableColumn_ReferencedDataType.md) | Property that returns the data type contained in the column. |
| [ReferencedObject](../iAssemblyTableColumn/iAssemblyTableColumn_ReferencedObject.md) | Property that returns the object referenced by the column. For instance, if the column references a fillet feature suppression, the corresponding FilletFeature object is returned. Similarly, if a file property is referenced, the corresponding Property object is returned.  The property returns Nothing if there is no corresponding object (e.g. when the ReferencedDataType returns kMemberNameColumn). |
| [Type](../iAssemblyTableColumn/iAssemblyTableColumn_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[iAssemblyFactory.FileNameColumn](../iAssemblyFactory/iAssemblyFactory_FileNameColumn.md), [iAssemblyTableColumns.Item](../iAssemblyTableColumns/iAssemblyTableColumns_Item.md)

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |