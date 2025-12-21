# ApprenticeServerDrawingDocument Object

Derived from: [ApprenticeServerDocument](../ApprenticeServerDocument/ApprenticeServerDocument.md) Object

## Description

The ApprenticeServerDrawingDocument object represents the drawing document within an Apprentice context, and provides access to the Sheets in the drawing.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Close](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_Close.md) | Closes this document. |
| [CreateHighlightSet](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_CreateHighlightSet.md) | Method that creates a new highlight set. |
| [FindWhereUsed](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_FindWhereUsed.md) | Method that obtains the set of documents that reference the given file within this document. |
| [GetLocationFoundIn](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_GetLocationFoundIn.md) | Obtains the name of the location this file was found in. |
| [RevertReservedForWriteByMe](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_RevertReservedForWriteByMe.md) | Method that reverts the file checked out by the caller. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveStandard](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ActiveStandard.md) | Gets the currently active drafting standard that applies to all of the sheets. |
| [AllReferencedDocuments](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_AllReferencedDocuments.md) | Property that returns all the document references of this document along with all of the recursively nested references. |
| [AttributeManager](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_AttributeManager.md) | Returns the AttributeManager object. |
| [AttributeSets](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ClientViews](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ClientViews.md) | Property that returns the document's . |
| [Compacted](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_Compacted.md) | Gets the Boolean that states whether this file has been processed for compaction since the last save. |
| [ComponentDefinition](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ComponentDefinition.md) | Gets the primary that resides in this file. |
| [ContainingDWGDocument](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ContainingDWGDocument.md) | Gets the reference to the containing DWG document when this document is stored in a DWG. |
| [DatabaseRevisionId](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_DatabaseRevisionId.md) | Gets the GUID that represents the last saved revision of database contained in this document. This revision id tracks modifications to the database (such as reference changes, geometry changes, etc.) but does not track file property changes. |
| [Dirty](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_Dirty.md) | Gets/Sets a Boolean flag indicating if the Document has been written into, since opened. |
| [DisplayName](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_DisplayName.md) | Gets/Sets the user-displayable name of this Document. Defaults to file-name. |
| [DocumentInterests](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_DocumentInterests.md) | Property that returns the DocumentInterests collection object. |
| [DocumentType](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_DocumentType.md) | Gets the constant that indicates the type of this document. |
| [File](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_File.md) | Property that returns the file (storage) on disk that contains this document. |
| [FilePropertySets](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_FilePropertySets.md) | Read-only property that returns the file PropertySets. This is equivalent to the iProperties that got from Shell Extension. |
| [FileSaveCounter](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_FileSaveCounter.md) | Gets the number that indicates the number of times the file has been saved. |
| [FullDocumentName](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_FullDocumentName.md) | Property that returns the fully qualified name of the document. The string is the full file name concatenated with the document name and is a unique identifier for the document. The document name is returned by the Name property on the Document object. |
| [FullFileName](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_FullFileName.md) | Gets the fully qualified file-name of this document. |
| [HealthStatus](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_InternalName.md) | Gets the Internal Name (a GUID) for this document. |
| [IsInventorDWG](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_IsInventorDWG.md) | Property that returns whether this is an Inventor DWG document. |
| [IsModifiable](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_IsModifiable.md) | Property that returns whether this document can be currently modified. One of the reasons a document may be non-modifiable is if any other document belonging to the file containing this document is currently being edited. |
| [IsSubstitutePart](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_IsSubstitutePart.md) | Read-only property that returns whether this part is intended to be used as a substitute part. (applies only to part documents). |
| [NeedsMigrating](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_NeedsMigrating.md) | Gets the Boolean indicating whether this file needs to be migrated first, using Autodesk Inventor (opened and saved using Autodesk Inventor), before any edits can be performed to the Autodesk Inventor-specific data within this file. |
| [Open](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_Open.md) | Property that returns whether this document is currently open. If False, the document has only been initialized and calling methods or properties on the document could cause it to open. |
| [PrintManager](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_PrintManager.md) | Property that returns the object for this document. |
| [PropertySets](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_PropertySets.md) | Gets the object that manages the File Properties. |
| [ReferencedDocumentDescriptors](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ReferencedDocumentDescriptors.md) | Property that returns an enumeration of descriptors that represent the native document references held by this document. |
| [ReferencedDocuments](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ReferencedDocuments.md) | Property that returns all the documents referenced by this document. |
| [ReferencedOLEFileDescriptors](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ReferencedOLEFileDescriptors.md) | Property that returns the collection of linked files in the document. Embeddings are not accessible in Apprentice. |
| [ReferencedOpaqueFileDescriptors](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ReferencedOpaqueFileDescriptors.md) | Gets the collection of descriptor objects, presenting (editable) information about opaque references held. |
| [ReferenceKeyManager](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ReferenceKeyManager.md) | Gets this Document's ReferenceKeyManager object. |
| [ReferencingDocuments](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ReferencingDocuments.md) | Property that returns all the documents in memory that reference this document. |
| [RequiresUpdate](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_RequiresUpdate.md) | Property that returns whether the document requires an update. Note that the document cannot be updated in Apprentice. |
| [ReservedForWrite](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ReservedForWrite.md) | Gets the Boolean flag indicating whether this file has been reserved for write by someone. |
| [ReservedForWriteByMe](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ReservedForWriteByMe.md) | Gets/Sets the Boolean flag indicating whether this file has been reserved for write by the caller. |
| [ReservedForWriteLogin](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ReservedForWriteLogin.md) | Gets the login of the person who currently holds the reservation to write. |
| [ReservedForWriteName](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ReservedForWriteName.md) | Gets the name of the person who currently holds the reservation to write. |
| [ReservedForWriteTime](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ReservedForWriteTime.md) | Gets the time at which the reservation was made. |
| [ReservedForWriteVersion](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_ReservedForWriteVersion.md) | Gets the version within this file that has been reserved for write. |
| [Sheets](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_Sheets.md) | Property that returns the collection of all the sheets making up this document. |
| [SoftwareVersionCreated](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_SoftwareVersionCreated.md) | Gets the object that encapsulates the version of the software with which this document was first created. |
| [SoftwareVersionSaved](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_SoftwareVersionSaved.md) | Gets the object that encapsulates the version of the software with which this document was last saved. |
| [Thumbnail](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_Thumbnail.md) | Property that returns a bitmap picture of the document. |
| [Type](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitsOfMeasure](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_UnitsOfMeasure.md) | Property that returns the UnitsOfMeasure object. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |