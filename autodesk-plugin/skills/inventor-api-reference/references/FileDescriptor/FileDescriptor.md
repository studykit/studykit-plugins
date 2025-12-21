# FileDescriptor Object

## Description

The FileDescriptor object represents a reference to an Autodesk Inventor file or a foreign file.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetCustomLogicalFileName](../FileDescriptor/FileDescriptor_GetCustomLogicalFileName.md) | Similar in nature to the Logical Filename, except that the application interprets and perhaps controls the location and access to the file being referenced. |
| [PutCustomLogicalFileName](../FileDescriptor/FileDescriptor_PutCustomLogicalFileName.md) | This method does the posting of the Custom Logical Filename referred to in GetCustomLogicalFileName. |
| [ReplaceReference](../FileDescriptor/FileDescriptor_ReplaceReference.md) | Method that replaces the referenced file. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FileDescriptor/FileDescriptor_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [FileSaveCounter](../FileDescriptor/FileDescriptor_FileSaveCounter.md) | Property that returns the save counter associated with the file. |
| [FullFileName](../FileDescriptor/FileDescriptor_FullFileName.md) | Property that returns the full path name of the file as currently found (or the last known full file name, if the reference is not found). |
| [LibraryName](../FileDescriptor/FileDescriptor_LibraryName.md) | Gets the name of the library this reference was resolved in. This property is only valid when ReferenceMissing is false. |
| [LocationType](../FileDescriptor/FileDescriptor_LocationType.md) | Gets the type of location this reference was resolved in. This property is only valid when ReferenceMissing is false. |
| [Parent](../FileDescriptor/FileDescriptor_Parent.md) | Property that returns the parent File object of this descriptor. |
| [ReferencedFile](../FileDescriptor/FileDescriptor_ReferencedFile.md) | Property that returns the File object being referenced. The property returns Nothing for foreign file references. |
| [ReferencedFileType](../FileDescriptor/FileDescriptor_ReferencedFileType.md) | Property that returns type of the referenced file. |
| [ReferenceDisabled](../FileDescriptor/FileDescriptor_ReferenceDisabled.md) | Gets whether the link to this file is disabled. |
| [ReferenceInternalNameDifferent](../FileDescriptor/FileDescriptor_ReferenceInternalNameDifferent.md) | Gets whether the internal name of the referenced file is different from the last time the parent (referencing) file was saved. A value of True indicates that the currently referenced file has a different internal name than the originally referenced file. |
| [ReferenceLocationDifferent](../FileDescriptor/FileDescriptor_ReferenceLocationDifferent.md) | Gets whether the file path or the file name of the referenced file is different from the last time the parent (referencing) file was saved. A value of True indicates that the currently referenced file has a different file path or file name. |
| [ReferenceMissing](../FileDescriptor/FileDescriptor_ReferenceMissing.md) | Property that returns whether the referenced file is missing (unresolved). |
| [RelativeFileName](../FileDescriptor/FileDescriptor_RelativeFileName.md) | Gets the relative file name from the resolved location of this reference. This property is only valid when ReferenceMissing is false. |
| [Type](../FileDescriptor/FileDescriptor_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BOMRow.ReferencedFileDescriptor](../BOMRow/BOMRow_ReferencedFileDescriptor.md), [DocumentDescriptor.ReferencedFileDescriptor](../DocumentDescriptor/DocumentDescriptor_ReferencedFileDescriptor.md), [FileDescriptorsEnumerator.Item](../FileDescriptorsEnumerator/FileDescriptorsEnumerator_Item.md), [ReferencedOLEFileDescriptor.FileDescriptor](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_FileDescriptor.md)

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |