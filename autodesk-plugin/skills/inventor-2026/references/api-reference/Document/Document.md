# Document Object

## Description

The Document object represents an in-memory Inventor document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../Document/Document_Activate.md) | Makes this document the active one (receives user-focus). |
| [Close](../Document/Document_Close.md) | Closes this document. |
| [CreateHighlightSet](../Document/Document_CreateHighlightSet.md) | Method that creates a new highlight set. |
| [FindWhereUsed](../Document/Document_FindWhereUsed.md) | Method that obtains the set of documents that reference the given file within this document. |
| [GetLocationFoundIn](../Document/Document_GetLocationFoundIn.md) | Obtains the name of the location this file was found in. |
| [GetMissingAddInBehavior](../Document/Document_GetMissingAddInBehavior.md) | Method that gets the commands disabled when a particular AddIn is absent. |
| [GetPrivateStorage](../Document/Document_GetPrivateStorage.md) | Obtains a private sub-storage within this document with the given name. Can create one, if one does not exist. |
| [GetPrivateStream](../Document/Document_GetPrivateStream.md) | Obtains a private stream within this document with the given name. Can create one, if one does not exist. |
| [HasPrivateStorage](../Document/Document_HasPrivateStorage.md) | Obtains a Boolean flag indicating if the specified sub-storage exists within this document. |
| [HasPrivateStream](../Document/Document_HasPrivateStream.md) | Obtains a Boolean flag indicating if the specified stream exists within this document. |
| [PutInternalNameAndRevisionId](../Document/Document_PutInternalNameAndRevisionId.md) | Constructs and sets the Internal Name and Revision Identifier for this Document from strings supplied. This can only be done on a previously un-saved document (New or SaveCopyAs) |
| [Rebuild](../Document/Document_Rebuild.md) | Performs compute operations on all of the entities within this document's scope as if all of the driving entities had been 'dirtied.' |
| [Rebuild2](../Document/Document_Rebuild2.md) | Method that performs compute operations on all of the entities within this Document's scope as if all of the driving entities had been 'dirtied'. |
| [ReleaseReference](../Document/Document_ReleaseReference.md) | Method that releases the reference that gets added if a document is opened invisibly through the API. Releasing the reference on a hidden document makes it a candidate for closure the next time Inventor closes all unreferenced documents. |
| [ResolveFile](../Document/Document_ResolveFile.md) | Method that invoke the resolve file for the document if there are references missing. |
| [RevertReservedForWriteByMe](../Document/Document_RevertReservedForWriteByMe.md) | Method that reverts the file checked out by the caller. |
| [Save](../Document/Document_Save.md) | Saves this document to disk. |
| [Save2](../Document/Document_Save2.md) | Method that saves the document and the specified dependent documents. |
| [SaveAs](../Document/Document_SaveAs.md) | Saves this document into a file of the specified name. |
| [SaveAs2](../Document/Document_SaveAs2.md) | Saves this document into a file of the specified name. |
| [SetMissingAddInBehavior](../Document/Document_SetMissingAddInBehavior.md) | Method that sets the commands to be disabled when a particular AddIn is absent. |
| [SetThumbnailSaveOption](../Document/Document_SetThumbnailSaveOption.md) | Method that sets the thumbnail (preview picture) save option. |
| [Update](../Document/Document_Update.md) | Performs compute operations on all of the entities within this Document's scope that may be out of date with respect to their driving entities. |
| [Update2](../Document/Document_Update2.md) | Method that performs compute operations on all of the entities within this Document's scope that may be out of date with respect to their driving entities. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActivatedObject](../Document/Document_ActivatedObject.md) | Gets the object that has been in-place activated for edit within the context of this document. |
| [AllReferencedDocuments](../Document/Document_AllReferencedDocuments.md) | Property that returns all the document references of this Document along with all of the recursively nested references. |
| [AttributeManager](../Document/Document_AttributeManager.md) | Returns the AttributeManager object. |
| [AttributeSets](../Document/Document_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BrowserPanes](../Document/Document_BrowserPanes.md) | Property that returns the  collection object. |
| [ClientViews](../Document/Document_ClientViews.md) | Returns document's client views. |
| [Compacted](../Document/Document_Compacted.md) | Gets the Boolean that states whether this file has been processed for compaction since the last save. |
| [DatabaseRevisionId](../Document/Document_DatabaseRevisionId.md) | Gets the GUID that represents the last saved revision of database contained in this document. This revision id tracks modifications to the database (such as reference changes, geometry changes, etc.) but does not track file property changes. |
| [DefaultCommand](../Document/Document_DefaultCommand.md) | Gets the default command for this document. |
| [Dirty](../Document/Document_Dirty.md) | Gets/Sets a Boolean flag indicating if the Document has been written into, since opened. |
| [DisabledCommandTypes](../Document/Document_DisabledCommandTypes.md) | Bit mask indicating the disabled command types. |
| [DisplayName](../Document/Document_DisplayName.md) | Gets/Sets the user-displayable name of this Document. Defaults to file-name. |
| [DisplayNameOverridden](../Document/Document_DisplayNameOverridden.md) | Read-write property that gets and sets whether the display name of the document has been overridden. |
| [DocumentEvents](../Document/Document_DocumentEvents.md) | This object supports a set of events that are specific to the document. |
| [DocumentInterests](../Document/Document_DocumentInterests.md) | Property that returns the DocumentInterests collection object. |
| [DocumentSubType](../Document/Document_DocumentSubType.md) | Property that returns the subtype of the document. |
| [DocumentType](../Document/Document_DocumentType.md) | Gets the constant that indicates the type of this document. |
| [File](../Document/Document_File.md) | Property that returns the file (storage) on disk that contains this document. |
| [FilePropertySets](../Document/Document_FilePropertySets.md) | Read-only property that returns the file PropertySets. This is equivalent to the iProperties that got from Shell Extension. |
| [FileSaveCounter](../Document/Document_FileSaveCounter.md) | Gets the number that indicates the number of times the file has been saved. |
| [FullDocumentName](../Document/Document_FullDocumentName.md) | Property that returns the fully qualified name of the document. The string is the full file name concatenated with the document name and is a unique identifier for the document. The document name is returned by the Name property on the Document object. |
| [FullFileName](../Document/Document_FullFileName.md) | Gets/Sets the fully qualified file-name of this Document. |
| [GraphicsDataSetsCollection](../Document/Document_GraphicsDataSetsCollection.md) | Property that returns the object for the document. |
| [HasReferencesMissing](../Document/Document_HasReferencesMissing.md) | Read-only property that returns whether there are references missing for this document. |
| [InternalName](../Document/Document_InternalName.md) | Gets the Internal Name (a GUID) for this document. |
| [IsModifiable](../Document/Document_IsModifiable.md) | Property that returns whether this document can be currently modified. One of the reasons a document may be non-modifiable is if any other document belonging to the file containing this document is currently being edited. |
| [ModelStateName](../Document/Document_ModelStateName.md) | Read-only property that returns the model state that this document represents. |
| [NeedsMigrating](../Document/Document_NeedsMigrating.md) | Property that returns whether the document needs to be migrated to the current release. |
| [NonTransactingClientGraphicsCollection](../Document/Document_NonTransactingClientGraphicsCollection.md) | Read-only property that returns the non-transacting ClientGraphicsCollection object. |
| [NonTransactingGraphicsDataSetsCollection](../Document/Document_NonTransactingGraphicsDataSetsCollection.md) | Read-only property that returns the non-transacting GraphicsDataSetsCollection object. |
| [Open](../Document/Document_Open.md) | Property that returns whether this document is currently open. If False, the document has only been initialized and calling methods or properties on the document could cause it to open. |
| [Parent](../Document/Document_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [PrintManager](../Document/Document_PrintManager.md) | Property that returns the PrintManager, or when called from a DrawingDocument it returns a DrawingPrintManager object. |
| [PropertySets](../Document/Document_PropertySets.md) | Gets the Property Sets object that controls the file's published-format properties. |
| [RecentChanges](../Document/Document_RecentChanges.md) | Gets a bit-encoded value where the bits indicate the kind of changes made to the document since it became dirty. |
| [ReferencedDocumentDescriptors](../Document/Document_ReferencedDocumentDescriptors.md) | Property that returns an enumeration of descriptors that represent the native document references held by this document. |
| [ReferencedDocuments](../Document/Document_ReferencedDocuments.md) | Property that returns all the documents directly referenced by this document. |
| [ReferencedOLEFileDescriptors](../Document/Document_ReferencedOLEFileDescriptors.md) | Property that returns the collection of linked and embedded files in the document. |
| [ReferencedOLEFileDescriptors2](../Document/Document_ReferencedOLEFileDescriptors2.md) | Gets the collection of OLE attachments made in this Document that match the input type. Returns all OLE attachments if type is kOLEDocumentUnknownObject. |
| [ReferencedOpaqueFileDescriptors](../Document/Document_ReferencedOpaqueFileDescriptors.md) | Gets the collection of descriptor objects, presenting (editable) information about opaque references held. |
| [ReferenceKeyManager](../Document/Document_ReferenceKeyManager.md) | Gets this document's ReferenceKeyManager. |
| [ReferencingDocuments](../Document/Document_ReferencingDocuments.md) | Property that returns all the documents in memory that reference this document. A referencing document may or may not be fully open (i.e. may just be initialized). |
| [RequiresUpdate](../Document/Document_RequiresUpdate.md) | Gets the Boolean indicating if any of the entities within this document's scope is out of date with respect to their driving entities. |
| [ReservedForWrite](../Document/Document_ReservedForWrite.md) | Gets the Boolean flag indicating whether this file has been reserved for write by someone. |
| [ReservedForWriteByMe](../Document/Document_ReservedForWriteByMe.md) | Gets/Sets the Boolean flag indicating whether this file has been reserved for write by the caller. |
| [ReservedForWriteLogin](../Document/Document_ReservedForWriteLogin.md) | Gets the login of the person who currently holds the reservation to write. |
| [ReservedForWriteName](../Document/Document_ReservedForWriteName.md) | Gets the name of the person who currently holds the reservation to write. |
| [ReservedForWriteTime](../Document/Document_ReservedForWriteTime.md) | Gets the time at which the reservation was made. |
| [ReservedForWriteVersion](../Document/Document_ReservedForWriteVersion.md) | Gets the version within this file that has been reserved for write. |
| [SelectionPreferences](../Document/Document_SelectionPreferences.md) | Gets the SelectionPreferences. |
| [SelectionPriority](../Document/Document_SelectionPriority.md) | Gets and sets the current selection priority for the document. |
| [SelectSet](../Document/Document_SelectSet.md) | Property that returns the SelectSet object. |
| [SoftwareVersionCreated](../Document/Document_SoftwareVersionCreated.md) | Gets the object that encapsulates the version of the software with which this document was first created. |
| [SoftwareVersionSaved](../Document/Document_SoftwareVersionSaved.md) | Gets the object that encapsulates the version of the software with which this document was last saved. |
| [SubType](../Document/Document_SubType.md) | Gets/Sets the sub-Type (a published GUID. See DocCLSIDs.h) of this Document. Setting a new sub-Type will invoke a validation sequence and may fail if the operation is invalid. |
| [Thumbnail](../Document/Document_Thumbnail.md) | Property that returns a bitmap picture of the document. |
| [ThumbnailSaveOption](../Document/Document_ThumbnailSaveOption.md) | Property that returns the current thumbnail (preview picture) save option. |
| [Type](../Document/Document_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitsOfMeasure](../Document/Document_UnitsOfMeasure.md) | Property that returns the UnitsOfMeasure object. |
| [VBAProject](../Document/Document_VBAProject.md) | Property that returns the Autodesk Inventor VBA project for this document. |
| [Views](../Document/Document_Views.md) | Gets all the open views of this document in a collection. |

## Accessed From

[Application.ActiveDocument](../Application/Application_ActiveDocument.md), [Application.ActiveEditDocument](../Application/Application_ActiveEditDocument.md), [AssemblyComponentDefinition.FactoryDocument](../AssemblyComponentDefinition/AssemblyComponentDefinition_FactoryDocument.md), [AssemblyDocument.EmbeddingDocument](../AssemblyDocument/AssemblyDocument_EmbeddingDocument.md), [BrowserNodeDefinition.Parent](../BrowserNodeDefinition/BrowserNodeDefinition_Parent.md), [BrowserPane.Parent](../BrowserPane/BrowserPane_Parent.md), [ClientBrowserNodeDefinition.Parent](../ClientBrowserNodeDefinition/ClientBrowserNodeDefinition_Parent.md), [ClientNodeResource.Parent](../ClientNodeResource/ClientNodeResource_Parent.md), [Documents.Add](../Documents/Documents_Add.md), [Documents.Item](../Documents/Documents_Item.md), [Documents.ItemByName](../Documents/Documents_ItemByName.md), [Documents.Open](../Documents/Documents_Open.md), [Documents.OpenWithOptions](../Documents/Documents_OpenWithOptions.md), [DocumentsEnumerator.Item](../DocumentsEnumerator/DocumentsEnumerator_Item.md), [EnvironmentManager.Parent](../EnvironmentManager/EnvironmentManager_Parent.md), [FileMetadata.Document](../FileMetadata/FileMetadata_Document.md), [FlatPatternSettings.Parent](../FlatPatternSettings/FlatPatternSettings_Parent.md), [InteractionEvents.TargetDocument](../InteractionEvents/InteractionEvents_TargetDocument.md), [ModelingSettings.Parent](../ModelingSettings/ModelingSettings_Parent.md), [ModelState.Document](../ModelState/ModelState_Document.md), [ModelState.FactoryDocument](../ModelState/ModelState_FactoryDocument.md), [NativeBrowserNodeDefinition.Parent](../NativeBrowserNodeDefinition/NativeBrowserNodeDefinition_Parent.md), [ObjectVisibility.Parent](../ObjectVisibility/ObjectVisibility_Parent.md), [OGSSceneNode.Document](OGSSceneNode_Document.md), [PartComponentDefinition.FactoryDocument](../PartComponentDefinition/PartComponentDefinition_FactoryDocument.md), [PartDocument.EmbeddingDocument](../PartDocument/PartDocument_EmbeddingDocument.md), [SheetMetalComponentDefinition.FactoryDocument](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_FactoryDocument.md), [Sketch3DSettings.Parent](../Sketch3DSettings/Sketch3DSettings_Parent.md), [SketchSettings.Parent](../SketchSettings/SketchSettings_Parent.md), [Transaction.Document](../Transaction/Transaction_Document.md), [View.Document](../View/View_Document.md), [View.Parent](../View/View_Parent.md), [WeldmentComponentDefinition.FactoryDocument](../WeldmentComponentDefinition/WeldmentComponentDefinition_FactoryDocument.md)

## Derived Classes

[AssemblyDocument](../AssemblyDocument/AssemblyDocument.md), [DrawingDocument](../DrawingDocument/DrawingDocument.md), [PartDocument](../PartDocument/PartDocument.md), [PresentationDocument](../PresentationDocument/PresentationDocument.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creation a balloon](../../sample-programs/Balloons_Add_Sample.md) | This sample demonstrates the creation of a balloon. |
| [Client Graphics - Draw Range Box](../../sample-programs/ClientGraphics_Sample.md) | This sample demonstrates the use of client graphics to draw the range box of selected entities. |

## Version

Introduced in version 4
