# PresentationDocument Object

Derived from: [Document](../Document/Document.md) Object

## Description

The PresentationDocument object respesents a presentation document in Inventor.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../PresentationDocument/PresentationDocument_Activate.md) | Makes this document the active one (receives user-focus). |
| [Close](../PresentationDocument/PresentationDocument_Close.md) | Closes this document. |
| [CreateHighlightSet](../PresentationDocument/PresentationDocument_CreateHighlightSet.md) | Method that creates a new highlight set. |
| [FindWhereUsed](../PresentationDocument/PresentationDocument_FindWhereUsed.md) | Method that obtains the set of documents that reference the given file within this document. |
| [GetLocationFoundIn](../PresentationDocument/PresentationDocument_GetLocationFoundIn.md) | Obtains the name of the location this file was found in. |
| [GetMissingAddInBehavior](../PresentationDocument/PresentationDocument_GetMissingAddInBehavior.md) | Method that gets the commands disabled when a particular AddIn is absent. |
| [GetPrivateStorage](../PresentationDocument/PresentationDocument_GetPrivateStorage.md) | Obtains a private sub-storage within this document with the given name. Can create one, if one does not exist. |
| [GetPrivateStream](../PresentationDocument/PresentationDocument_GetPrivateStream.md) | Obtains a private stream within this document with the given name. Can create one, if one does not exist. |
| [HasPrivateStorage](../PresentationDocument/PresentationDocument_HasPrivateStorage.md) | Obtains a Boolean flag indicating if the specified sub-storage exists within this document. |
| [HasPrivateStream](../PresentationDocument/PresentationDocument_HasPrivateStream.md) | Obtains a Boolean flag indicating if the specified stream exists within this document. |
| [PutInternalNameAndRevisionId](../PresentationDocument/PresentationDocument_PutInternalNameAndRevisionId.md) | Constructs and sets the Internal Name and Revision Identifier for this Document from strings supplied. This can only be done on a previously un-saved document (New or SaveCopyAs) |
| [Rebuild](../PresentationDocument/PresentationDocument_Rebuild.md) | Performs compute operations on all of the entities within this document's scope as if all of the driving entities had been 'dirtied.' |
| [Rebuild2](../PresentationDocument/PresentationDocument_Rebuild2.md) | Method that performs compute operations on all of the entities within this Document's scope as if all of the driving entities had been 'dirtied'. |
| [ReleaseReference](../PresentationDocument/PresentationDocument_ReleaseReference.md) | Method that releases the reference that gets added if a document is opened invisibly through the API. Releasing the reference on a hidden document makes it a candidate for closure the next time Inventor closes all unreferenced documents. |
| [ResolveFile](../PresentationDocument/PresentationDocument_ResolveFile.md) | Method that invoke the resolve file for the document if there are references missing. |
| [RevertReservedForWriteByMe](../PresentationDocument/PresentationDocument_RevertReservedForWriteByMe.md) | Method that reverts the file checked out by the caller. |
| [Save](../PresentationDocument/PresentationDocument_Save.md) | Saves this document to disk. |
| [Save2](../PresentationDocument/PresentationDocument_Save2.md) | Method that saves the document and the specified dependent documents. |
| [SaveAs](../PresentationDocument/PresentationDocument_SaveAs.md) | Saves this document into a file of the specified name. |
| [SaveAs2](../PresentationDocument/PresentationDocument_SaveAs2.md) | Saves this document into a file of the specified name. |
| [SetMissingAddInBehavior](../PresentationDocument/PresentationDocument_SetMissingAddInBehavior.md) | Method that sets the commands to be disabled when a particular AddIn is absent. |
| [SetThumbnailSaveOption](../PresentationDocument/PresentationDocument_SetThumbnailSaveOption.md) | Method that sets the thumbnail (preview picture) save option. |
| [Update](../PresentationDocument/PresentationDocument_Update.md) | Performs compute operations on all of the entities within this Document's scope that may be out of date with respect to their driving entities. |
| [Update2](../PresentationDocument/PresentationDocument_Update2.md) | Method that performs compute operations on all of the entities within this Document's scope that may be out of date with respect to their driving entities. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActivatedObject](../PresentationDocument/PresentationDocument_ActivatedObject.md) | Gets the object that has been in-place activated for edit within the context of this document. |
| [ActiveLightingStyle](../PresentationDocument/PresentationDocument_ActiveLightingStyle.md) | Gets and sets the lighting style to use for the presentation. |
| [ActiveScene](../PresentationDocument/PresentationDocument_ActiveScene.md) | Read-only property that returns the active PresentationScene object. |
| [AllReferencedDocuments](../PresentationDocument/PresentationDocument_AllReferencedDocuments.md) | Property that returns all the document references of this Document along with all of the recursively nested references. |
| [AppearanceAssets](../PresentationDocument/PresentationDocument_AppearanceAssets.md) | Gets an AssetsEnumerator collection object that contains the appearances associated with the document. |
| [AttributeManager](../PresentationDocument/PresentationDocument_AttributeManager.md) | Returns the AttributeManager object. |
| [AttributeSets](../PresentationDocument/PresentationDocument_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BrowserPanes](../PresentationDocument/PresentationDocument_BrowserPanes.md) | Property that returns the  collection object. |
| [ClientViews](../PresentationDocument/PresentationDocument_ClientViews.md) | Returns document's client views. |
| [Compacted](../PresentationDocument/PresentationDocument_Compacted.md) | Gets the Boolean that states whether this file has been processed for compaction since the last save. |
| [DatabaseRevisionId](../PresentationDocument/PresentationDocument_DatabaseRevisionId.md) | Gets the GUID that represents the last saved revision of database contained in this document. This revision id tracks modifications to the database (such as reference changes, geometry changes, etc.) but does not track file property changes. |
| [DefaultCommand](../PresentationDocument/PresentationDocument_DefaultCommand.md) | Gets the default command for this document. |
| [Dirty](../PresentationDocument/PresentationDocument_Dirty.md) | Gets/Sets a Boolean flag indicating if the Document has been written into, since opened. |
| [DisabledCommandList](../PresentationDocument/PresentationDocument_DisabledCommandList.md) | Property that returns the DisabledCommandList object. This object allows the document to disable specific commands. This list contains commands that are disabled in addition to those specified by the DisabledCommandTypes property. |
| [DisabledCommandTypes](../PresentationDocument/PresentationDocument_DisabledCommandTypes.md) | Bit mask indicating the disabled command types. |
| [DisplayName](../PresentationDocument/PresentationDocument_DisplayName.md) | Gets/Sets the user-displayable name of this Document. Defaults to file-name. |
| [DisplayNameOverridden](../PresentationDocument/PresentationDocument_DisplayNameOverridden.md) | Read-write property that gets and sets whether the display name of the document has been overridden. |
| [DisplaySettings](../PresentationDocument/PresentationDocument_DisplaySettings.md) | Property that returns the DisplaySettings object. The DisplaySettings object provides access to various display appearance related document settings. |
| [DocumentEvents](../PresentationDocument/PresentationDocument_DocumentEvents.md) | This object supports a set of events that are specific to the document. |
| [DocumentInterests](../PresentationDocument/PresentationDocument_DocumentInterests.md) | Property that returns the DocumentInterests collection object. |
| [DocumentSubType](../PresentationDocument/PresentationDocument_DocumentSubType.md) | Property that returns the subtype of the document. |
| [DocumentType](../PresentationDocument/PresentationDocument_DocumentType.md) | Gets the constant that indicates the type of this document. |
| [EnvironmentManager](../PresentationDocument/PresentationDocument_EnvironmentManager.md) |  |
| [File](../PresentationDocument/PresentationDocument_File.md) | Property that returns the file (storage) on disk that contains this document. |
| [FilePropertySets](../PresentationDocument/PresentationDocument_FilePropertySets.md) | Read-only property that returns the file PropertySets. This is equivalent to the iProperties that got from Shell Extension. |
| [FileSaveCounter](../PresentationDocument/PresentationDocument_FileSaveCounter.md) | Gets the number that indicates the number of times the file has been saved. |
| [FullDocumentName](../PresentationDocument/PresentationDocument_FullDocumentName.md) | Property that returns the fully qualified name of the document. The string is the full file name concatenated with the document name and is a unique identifier for the document. The document name is returned by the Name property on the Document object. |
| [FullFileName](../PresentationDocument/PresentationDocument_FullFileName.md) | Gets/Sets the fully qualified file-name of this Document. |
| [GraphicsDataSetsCollection](../PresentationDocument/PresentationDocument_GraphicsDataSetsCollection.md) | Property that returns the object for the document. |
| [HasReferencesMissing](../PresentationDocument/PresentationDocument_HasReferencesMissing.md) | Read-only property that returns whether there are references missing for this document. |
| [InternalName](../PresentationDocument/PresentationDocument_InternalName.md) | Gets the Internal Name (a GUID) for this document. |
| [IsModifiable](../PresentationDocument/PresentationDocument_IsModifiable.md) | Property that returns whether this document can be currently modified. One of the reasons a document may be non-modifiable is if any other document belonging to the file containing this document is currently being edited. |
| [LightingStyles](../PresentationDocument/PresentationDocument_LightingStyles.md) | Property that returns the LightingStyles collection object. |
| [ModelStateName](../PresentationDocument/PresentationDocument_ModelStateName.md) | Read-only property that returns the model state that this document represents. |
| [NeedsMigrating](../PresentationDocument/PresentationDocument_NeedsMigrating.md) | Property that returns whether the document needs to be migrated to the current release. |
| [NonTransactingClientGraphicsCollection](../PresentationDocument/PresentationDocument_NonTransactingClientGraphicsCollection.md) | Read-only property that returns the non-transacting ClientGraphicsCollection object. |
| [NonTransactingGraphicsDataSetsCollection](../PresentationDocument/PresentationDocument_NonTransactingGraphicsDataSetsCollection.md) | Read-only property that returns the non-transacting GraphicsDataSetsCollection object. |
| [Open](../PresentationDocument/PresentationDocument_Open.md) | Property that returns whether this document is currently open. If False, the document has only been initialized and calling methods or properties on the document could cause it to open. |
| [Parent](../PresentationDocument/PresentationDocument_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [PrintManager](../PresentationDocument/PresentationDocument_PrintManager.md) | Property that returns the PrintManager, or when called from a DrawingDocument it returns a DrawingPrintManager object. |
| [PropertySets](../PresentationDocument/PresentationDocument_PropertySets.md) | Gets the Property Sets object that controls the file's published-format properties. |
| [RecentChanges](../PresentationDocument/PresentationDocument_RecentChanges.md) | Gets a bit-encoded value where the bits indicate the kind of changes made to the document since it became dirty. |
| [ReferencedDocumentDescriptors](../PresentationDocument/PresentationDocument_ReferencedDocumentDescriptors.md) | Property that returns an enumeration of descriptors that represent the native document references held by this document. |
| [ReferencedDocuments](../PresentationDocument/PresentationDocument_ReferencedDocuments.md) | Property that returns all the documents directly referenced by this document. |
| [ReferencedOLEFileDescriptors](../PresentationDocument/PresentationDocument_ReferencedOLEFileDescriptors.md) | Property that returns the collection of linked and embedded files in the document. |
| [ReferencedOLEFileDescriptors2](../PresentationDocument/PresentationDocument_ReferencedOLEFileDescriptors2.md) | Gets the collection of OLE attachments made in this Document that match the input type. Returns all OLE attachments if type is kOLEDocumentUnknownObject. |
| [ReferencedOpaqueFileDescriptors](../PresentationDocument/PresentationDocument_ReferencedOpaqueFileDescriptors.md) | Gets the collection of descriptor objects, presenting (editable) information about opaque references held. |
| [ReferenceKeyManager](../PresentationDocument/PresentationDocument_ReferenceKeyManager.md) | Gets this document's ReferenceKeyManager. |
| [ReferencingDocuments](../PresentationDocument/PresentationDocument_ReferencingDocuments.md) | Property that returns all the documents in memory that reference this document. A referencing document may or may not be fully open (i.e. may just be initialized). |
| [RequiresUpdate](../PresentationDocument/PresentationDocument_RequiresUpdate.md) | Gets the Boolean indicating if any of the entities within this document's scope is out of date with respect to their driving entities. |
| [ReservedForWrite](../PresentationDocument/PresentationDocument_ReservedForWrite.md) | Gets the Boolean flag indicating whether this file has been reserved for write by someone. |
| [ReservedForWriteByMe](../PresentationDocument/PresentationDocument_ReservedForWriteByMe.md) | Gets/Sets the Boolean flag indicating whether this file has been reserved for write by the caller. |
| [ReservedForWriteLogin](../PresentationDocument/PresentationDocument_ReservedForWriteLogin.md) | Gets the login of the person who currently holds the reservation to write. |
| [ReservedForWriteName](../PresentationDocument/PresentationDocument_ReservedForWriteName.md) | Gets the name of the person who currently holds the reservation to write. |
| [ReservedForWriteTime](../PresentationDocument/PresentationDocument_ReservedForWriteTime.md) | Gets the time at which the reservation was made. |
| [ReservedForWriteVersion](../PresentationDocument/PresentationDocument_ReservedForWriteVersion.md) | Gets the version within this file that has been reserved for write. |
| [Scenes](../PresentationDocument/PresentationDocument_Scenes.md) | Read-only property that returns the PresentationScenes collection object. |
| [SelectionPreferences](../PresentationDocument/PresentationDocument_SelectionPreferences.md) | Gets the SelectionPreferences. |
| [SelectionPriority](../PresentationDocument/PresentationDocument_SelectionPriority.md) | Gets and sets the current selection priority for the document. |
| [SelectSet](../PresentationDocument/PresentationDocument_SelectSet.md) | Property that returns the SelectSet object. |
| [SoftwareVersionCreated](../PresentationDocument/PresentationDocument_SoftwareVersionCreated.md) | Gets the object that encapsulates the version of the software with which this document was first created. |
| [SoftwareVersionSaved](../PresentationDocument/PresentationDocument_SoftwareVersionSaved.md) | Gets the object that encapsulates the version of the software with which this document was last saved. |
| [SubType](../PresentationDocument/PresentationDocument_SubType.md) | Gets/Sets the sub-Type (a published GUID. See DocCLSIDs.h) of this Document. Setting a new sub-Type will invoke a validation sequence and may fail if the operation is invalid. |
| [Thumbnail](../PresentationDocument/PresentationDocument_Thumbnail.md) | Property that returns a bitmap picture of the document. |
| [ThumbnailSaveOption](../PresentationDocument/PresentationDocument_ThumbnailSaveOption.md) | Property that returns the current thumbnail (preview picture) save option. |
| [Type](../PresentationDocument/PresentationDocument_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitsOfMeasure](../PresentationDocument/PresentationDocument_UnitsOfMeasure.md) | Property that returns the UnitsOfMeasure object. |
| [VBAProject](../PresentationDocument/PresentationDocument_VBAProject.md) | Property that returns the Autodesk Inventor VBA project for this document. |
| [Views](../PresentationDocument/PresentationDocument_Views.md) | Gets all the open views of this document in a collection. |

## Accessed From

[PresentationScene.Parent](../PresentationScene/PresentationScene_Parent.md), [Publication.Parent](Publication_Parent.md)

## Version

Introduced in version 4
