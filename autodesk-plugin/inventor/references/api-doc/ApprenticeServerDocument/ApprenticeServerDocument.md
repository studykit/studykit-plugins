# ApprenticeServerDocument Object

## Description

The ApprenticeServerDocument object represents an in-memory Inventor document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Close](../ApprenticeServerDocument/ApprenticeServerDocument_Close.md) | Closes this document. |
| [CreateHighlightSet](../ApprenticeServerDocument/ApprenticeServerDocument_CreateHighlightSet.md) | Method that creates a new highlight set. |
| [FindWhereUsed](../ApprenticeServerDocument/ApprenticeServerDocument_FindWhereUsed.md) | Method that obtains the set of documents that reference the given file within this document. |
| [GetLocationFoundIn](../ApprenticeServerDocument/ApprenticeServerDocument_GetLocationFoundIn.md) | Obtains the name of the location this file was found in. |
| [RevertReservedForWriteByMe](../ApprenticeServerDocument/ApprenticeServerDocument_RevertReservedForWriteByMe.md) | Method that reverts the file checked out by the caller. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllReferencedDocuments](../ApprenticeServerDocument/ApprenticeServerDocument_AllReferencedDocuments.md) | Property that returns all the document references of this document along with all of the recursively nested references. |
| [AttributeManager](../ApprenticeServerDocument/ApprenticeServerDocument_AttributeManager.md) | Returns the AttributeManager object. |
| [AttributeSets](../ApprenticeServerDocument/ApprenticeServerDocument_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ClientViews](../ApprenticeServerDocument/ApprenticeServerDocument_ClientViews.md) | Property that returns the document's . |
| [Compacted](../ApprenticeServerDocument/ApprenticeServerDocument_Compacted.md) | Gets the Boolean that states whether this file has been processed for compaction since the last save. |
| [ComponentDefinition](../ApprenticeServerDocument/ApprenticeServerDocument_ComponentDefinition.md) | Gets the primary that resides in this file. |
| [DatabaseRevisionId](../ApprenticeServerDocument/ApprenticeServerDocument_DatabaseRevisionId.md) | Gets the GUID that represents the last saved revision of database contained in this document. This revision id tracks modifications to the database (such as reference changes, geometry changes, etc.) but does not track file property changes. |
| [Dirty](../ApprenticeServerDocument/ApprenticeServerDocument_Dirty.md) | Gets/Sets a Boolean flag indicating if the Document has been written into, since opened. |
| [DisplayName](../ApprenticeServerDocument/ApprenticeServerDocument_DisplayName.md) | Gets/Sets the user-displayable name of this Document. Defaults to file-name. |
| [DocumentInterests](../ApprenticeServerDocument/ApprenticeServerDocument_DocumentInterests.md) | Property that returns the DocumentInterests collection object. |
| [DocumentType](../ApprenticeServerDocument/ApprenticeServerDocument_DocumentType.md) | Gets the constant that indicates the type of this document. |
| [File](../ApprenticeServerDocument/ApprenticeServerDocument_File.md) | Property that returns the file (storage) on disk that contains this document. |
| [FilePropertySets](../ApprenticeServerDocument/ApprenticeServerDocument_FilePropertySets.md) | Read-only property that returns the file PropertySets. This is equivalent to the iProperties that got from Shell Extension. |
| [FileSaveCounter](../ApprenticeServerDocument/ApprenticeServerDocument_FileSaveCounter.md) | Gets the number that indicates the number of times the file has been saved. |
| [FullDocumentName](../ApprenticeServerDocument/ApprenticeServerDocument_FullDocumentName.md) | Property that returns the fully qualified name of the document. The string is the full file name concatenated with the document name and is a unique identifier for the document. The document name is returned by the Name property on the Document object. |
| [FullFileName](../ApprenticeServerDocument/ApprenticeServerDocument_FullFileName.md) | Gets the fully qualified file-name of this document. |
| [HealthStatus](../ApprenticeServerDocument/ApprenticeServerDocument_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ApprenticeServerDocument/ApprenticeServerDocument_InternalName.md) | Gets the Internal Name (a GUID) for this document. |
| [IsModifiable](../ApprenticeServerDocument/ApprenticeServerDocument_IsModifiable.md) | Property that returns whether this document can be currently modified. One of the reasons a document may be non-modifiable is if any other document belonging to the file containing this document is currently being edited. |
| [IsSubstitutePart](../ApprenticeServerDocument/ApprenticeServerDocument_IsSubstitutePart.md) | Read-only property that returns whether this part is intended to be used as a substitute part. (applies only to part documents). |
| [NeedsMigrating](../ApprenticeServerDocument/ApprenticeServerDocument_NeedsMigrating.md) | Gets the Boolean indicating whether this file needs to be migrated first, using Autodesk Inventor (opened and saved using Autodesk Inventor), before any edits can be performed to the Autodesk Inventor-specific data within this file. |
| [Open](../ApprenticeServerDocument/ApprenticeServerDocument_Open.md) | Property that returns whether this document is currently open. If False, the document has only been initialized and calling methods or properties on the document could cause it to open. |
| [PrintManager](../ApprenticeServerDocument/ApprenticeServerDocument_PrintManager.md) | Property that returns the object for this document. |
| [PropertySets](../ApprenticeServerDocument/ApprenticeServerDocument_PropertySets.md) | Gets the object that manages the File Properties. |
| [ReferencedDocumentDescriptors](../ApprenticeServerDocument/ApprenticeServerDocument_ReferencedDocumentDescriptors.md) | Property that returns an enumeration of descriptors that represent the native document references held by this document. |
| [ReferencedDocuments](../ApprenticeServerDocument/ApprenticeServerDocument_ReferencedDocuments.md) | Property that returns all the documents referenced by this document. |
| [ReferencedOLEFileDescriptors](../ApprenticeServerDocument/ApprenticeServerDocument_ReferencedOLEFileDescriptors.md) | Property that returns the collection of linked files in the document. Embeddings are not accessible in Apprentice. |
| [ReferencedOpaqueFileDescriptors](../ApprenticeServerDocument/ApprenticeServerDocument_ReferencedOpaqueFileDescriptors.md) | Gets the collection of descriptor objects, presenting (editable) information about opaque references held. |
| [ReferenceKeyManager](../ApprenticeServerDocument/ApprenticeServerDocument_ReferenceKeyManager.md) | Gets this Document's ReferenceKeyManager object. |
| [ReferencingDocuments](../ApprenticeServerDocument/ApprenticeServerDocument_ReferencingDocuments.md) | Property that returns all the documents in memory that reference this document. |
| [RequiresUpdate](../ApprenticeServerDocument/ApprenticeServerDocument_RequiresUpdate.md) | Property that returns whether the document requires an update. Note that the document cannot be updated in Apprentice. |
| [ReservedForWrite](../ApprenticeServerDocument/ApprenticeServerDocument_ReservedForWrite.md) | Gets the Boolean flag indicating whether this file has been reserved for write by someone. |
| [ReservedForWriteByMe](../ApprenticeServerDocument/ApprenticeServerDocument_ReservedForWriteByMe.md) | Gets/Sets the Boolean flag indicating whether this file has been reserved for write by the caller. |
| [ReservedForWriteLogin](../ApprenticeServerDocument/ApprenticeServerDocument_ReservedForWriteLogin.md) | Gets the login of the person who currently holds the reservation to write. |
| [ReservedForWriteName](../ApprenticeServerDocument/ApprenticeServerDocument_ReservedForWriteName.md) | Gets the name of the person who currently holds the reservation to write. |
| [ReservedForWriteTime](../ApprenticeServerDocument/ApprenticeServerDocument_ReservedForWriteTime.md) | Gets the time at which the reservation was made. |
| [ReservedForWriteVersion](../ApprenticeServerDocument/ApprenticeServerDocument_ReservedForWriteVersion.md) | Gets the version within this file that has been reserved for write. |
| [SoftwareVersionCreated](../ApprenticeServerDocument/ApprenticeServerDocument_SoftwareVersionCreated.md) | Gets the object that encapsulates the version of the software with which this document was first created. |
| [SoftwareVersionSaved](../ApprenticeServerDocument/ApprenticeServerDocument_SoftwareVersionSaved.md) | Gets the object that encapsulates the version of the software with which this document was last saved. |
| [Thumbnail](../ApprenticeServerDocument/ApprenticeServerDocument_Thumbnail.md) | Property that returns a bitmap picture of the document. |
| [Type](../ApprenticeServerDocument/ApprenticeServerDocument_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitsOfMeasure](../ApprenticeServerDocument/ApprenticeServerDocument_UnitsOfMeasure.md) | Property that returns the UnitsOfMeasure object. |

## Accessed From

[ApprenticeServer.Document](../ApprenticeServer/ApprenticeServer_Document.md), [ApprenticeServer.Open](../ApprenticeServer/ApprenticeServer_Open.md), [ApprenticeServer.OpenWithOptions](../ApprenticeServer/ApprenticeServer_OpenWithOptions.md), [ApprenticeServerComponent.Document](../ApprenticeServerComponent/ApprenticeServerComponent_Document.md), [ApprenticeServerComponent.Open](../ApprenticeServerComponent/ApprenticeServerComponent_Open.md), [ApprenticeServerComponent.OpenWithOptions](../ApprenticeServerComponent/ApprenticeServerComponent_OpenWithOptions.md), [ApprenticeServerDocuments.Item](../ApprenticeServerDocuments/ApprenticeServerDocuments_Item.md)

## Derived Classes

[ApprenticeServerDrawingDocument](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Update iProperty values using Apprentice](../../sample-programs/iPropertyApprentice_Sample.md) | Updates some iProperty values using Apprentice. The document specified in the code for the Open method must exist. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |