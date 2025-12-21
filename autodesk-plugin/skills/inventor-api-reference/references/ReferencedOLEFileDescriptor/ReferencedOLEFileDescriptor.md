# ReferencedOLEFileDescriptor Object

## Description

The ReferencedOLEFileDescriptor object represents an OLE reference to another file.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_Activate.md) | Method that causes the OLE file to be activated by the process currently registered to handle that type of document. |
| [Delete](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_Delete.md) | Method that deletes the reference file attachment. |
| [GetReferenceKey](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BrowserVisible](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_BrowserVisible.md) | Gets/Sets visible of the file reference in 3rdPartyFolder. |
| [DisplayName](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_DisplayName.md) | Gets/Sets the display name of the file as currently found (or the last known display name, if reference is not found). |
| [FileDescriptor](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_FileDescriptor.md) | Property that returns the corresponding FileDescriptor object. The ReplaceReference method on the returned object can be used to replace the referenced file. This property returns Nothing for embeddings. |
| [FullFileName](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_FullFileName.md) | Property that returns the full path name of the file as currently found (or the last known full file name, if reference is not found). This property returns a null string for an embedding descriptor. |
| [LastKnownFileTime](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_LastKnownFileTime.md) | Property that returns the time stamp on the file when it was last reviewed. This property returns Nothing for embeddings. |
| [LogicalName](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_LogicalName.md) | Property that returns the logical name of the reference. This is essentially the relative path used by Autodesk Inventor to find the file using the project paths as the search paths. |
| [OLEDocumentType](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_OLEDocumentType.md) | Property that returns the type of OLE reference this represents. Valid values are kOLEDocumentEmbeddingObject, kOLEDocumentLinkObject, or kOLEDocumentUnknownObject. |
| [Parent](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_Parent.md) | Property that returns the parent Document (in Inventor) or ApprenticeServerDocument (in Apprentice). |
| [ReferenceMonitoring](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_ReferenceMonitoring.md) | Gets/Sets whether the referenced file is monitored by Inventor for changes. |
| [ReferenceStatus](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_ReferenceStatus.md) | Property that returns the current status of the file reference. This property returns kUpToDateReference for embeddings. |
| [Type](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ReferencedOLEFileDescriptor/ReferencedOLEFileDescriptor_Visible.md) | Gets/Sets whether the linked/embedded object is visible in the graphics window. |

## Accessed From

[ParameterTable.ReferencedFileDescriptor](../ParameterTable/ParameterTable_ReferencedFileDescriptor.md), [ReferencedOLEFileDescriptors.Add](../ReferencedOLEFileDescriptors/ReferencedOLEFileDescriptors_Add.md), [ReferencedOLEFileDescriptors.Item](../ReferencedOLEFileDescriptors/ReferencedOLEFileDescriptors_Item.md), [ReferencedOLEFileDescriptors.ItemByName](../ReferencedOLEFileDescriptors/ReferencedOLEFileDescriptors_ItemByName.md), [SketchImage.ReferencedFileDescriptor](../SketchImage/SketchImage_ReferencedFileDescriptor.md), [SketchImageProxy.ReferencedFileDescriptor](../SketchImageProxy/SketchImageProxy_ReferencedFileDescriptor.md)

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |