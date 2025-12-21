# PartDocument Object

Derived from: [Document](../Document/Document.md) Object

## Description

The PartDocument object is derived from the Document object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../PartDocument/PartDocument_Activate.md) | Makes this document the active one (receives user-focus). |
| [Close](../PartDocument/PartDocument_Close.md) | Closes this document. |
| [CreateHighlightSet](../PartDocument/PartDocument_CreateHighlightSet.md) | Method that creates a new highlight set. |
| [FindWhereUsed](../PartDocument/PartDocument_FindWhereUsed.md) | Method that obtains the set of documents that reference the given file within this document. |
| [GetLocationFoundIn](../PartDocument/PartDocument_GetLocationFoundIn.md) | Obtains the name of the location this file was found in. |
| [GetMissingAddInBehavior](../PartDocument/PartDocument_GetMissingAddInBehavior.md) | Method that gets the commands disabled when a particular AddIn is absent. |
| [GetPrivateStorage](../PartDocument/PartDocument_GetPrivateStorage.md) | Obtains a private sub-storage within this document with the given name. Can create one, if one does not exist. |
| [GetPrivateStream](../PartDocument/PartDocument_GetPrivateStream.md) | Obtains a private stream within this document with the given name. Can create one, if one does not exist. |
| [GetSelectedObject](../PartDocument/PartDocument_GetSelectedObject.md) | In order to provide better handling of system resources Inventor does not load all of the data when a document is opened but delays loading information until it is needed. A common need in many programs is to have the user select vertices on parts. Instead of loading the part model in order to return the true selected Vertex, Inventor returns a GenericObject. You can use this method to obtain more information about the selected object. If it is a vertex you can get the point coordinates without forcing the entire model to be loaded, or if you do need to do additional processing that requires access to the full model you can also force that by using the "SelectedObject" argument. |
| [HasPrivateStorage](../PartDocument/PartDocument_HasPrivateStorage.md) | Obtains a Boolean flag indicating if the specified sub-storage exists within this document. |
| [HasPrivateStream](../PartDocument/PartDocument_HasPrivateStream.md) | Obtains a Boolean flag indicating if the specified stream exists within this document. |
| [PutGraphicsLevelsOfDetail](../PartDocument/PartDocument_PutGraphicsLevelsOfDetail.md) | Sets the graphics facet groups that must be saved with this file. Each bit indicating a level of detail. Up to 6 permitted. File size affected adversely when more. Recommend pick from GraphicsLevelsOfDetailEnum. |
| [PutInternalNameAndRevisionId](../PartDocument/PartDocument_PutInternalNameAndRevisionId.md) | Constructs and sets the Internal Name and Revision Identifier for this Document from strings supplied. This can only be done on a previously un-saved document (New or SaveCopyAs) |
| [Rebuild](../PartDocument/PartDocument_Rebuild.md) | Performs compute operations on all of the entities within this document's scope as if all of the driving entities had been 'dirtied.' |
| [Rebuild2](../PartDocument/PartDocument_Rebuild2.md) | Method that performs compute operations on all of the entities within this Document's scope as if all of the driving entities had been 'dirtied'. |
| [ReleaseReference](../PartDocument/PartDocument_ReleaseReference.md) | Method that releases the reference that gets added if a document is opened invisibly through the API. Releasing the reference on a hidden document makes it a candidate for closure the next time Inventor closes all unreferenced documents. |
| [ResolveFile](../PartDocument/PartDocument_ResolveFile.md) | Method that invoke the resolve file for the document if there are references missing. |
| [RevertReservedForWriteByMe](../PartDocument/PartDocument_RevertReservedForWriteByMe.md) | Method that reverts the file checked out by the caller. |
| [Save](../PartDocument/PartDocument_Save.md) | Saves this document to disk. |
| [Save2](../PartDocument/PartDocument_Save2.md) | Method that saves the document and the specified dependent documents. |
| [SaveAs](../PartDocument/PartDocument_SaveAs.md) | Saves this document into a file of the specified name. |
| [SaveAs2](../PartDocument/PartDocument_SaveAs2.md) | Saves this document into a file of the specified name. |
| [SetMissingAddInBehavior](../PartDocument/PartDocument_SetMissingAddInBehavior.md) | Method that sets the commands to be disabled when a particular AddIn is absent. |
| [SetThumbnailSaveOption](../PartDocument/PartDocument_SetThumbnailSaveOption.md) | Method that sets the thumbnail (preview picture) save option. |
| [Update](../PartDocument/PartDocument_Update.md) | Performs compute operations on all of the entities within this Document's scope that may be out of date with respect to their driving entities. |
| [Update2](../PartDocument/PartDocument_Update2.md) | Method that performs compute operations on all of the entities within this Document's scope that may be out of date with respect to their driving entities. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActivatedObject](../PartDocument/PartDocument_ActivatedObject.md) | Gets the object that has been in-place activated for edit within the context of this document. |
| [ActiveAppearance](../PartDocument/PartDocument_ActiveAppearance.md) | Gets and sets the default appearance for the part. |
| [ActiveLightingStyle](../PartDocument/PartDocument_ActiveLightingStyle.md) | Gets the active lighting style object. |
| [ActiveMarkStyle](../PartDocument/PartDocument_ActiveMarkStyle.md) | Property to get or set the active mark style object. |
| [ActiveMaterial](../PartDocument/PartDocument_ActiveMaterial.md) | Gets and sets the default material for the part. |
| [AllReferencedDocuments](../PartDocument/PartDocument_AllReferencedDocuments.md) | Property that returns all the document references of this Document along with all of the recursively nested references. |
| [AppearanceAssets](../PartDocument/PartDocument_AppearanceAssets.md) | Returns Assets collection object that contains the appearances associated with the document. |
| [AppearanceSourceType](../PartDocument/PartDocument_AppearanceSourceType.md) | Gets and sets the source of the appearance for the part. Setting to kMaterialAppearance will clear appearance override so the document uses the appearance associated with active material. |
| [Assets](../PartDocument/PartDocument_Assets.md) | Read-only property that returns an Assets collection object that contains all of the assets, regardless of their type, that are associated with the document. |
| [AssociativeForeignFilename](../PartDocument/PartDocument_AssociativeForeignFilename.md) | Read-only property that returns the full file name of the associative foreign file. This property returns empty string if the IsEmbeddedDocument returns False. |
| [AttributeManager](../PartDocument/PartDocument_AttributeManager.md) | Returns the AttributeManager object. |
| [AttributeSets](../PartDocument/PartDocument_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BrowserPanes](../PartDocument/PartDocument_BrowserPanes.md) | Property that returns the  collection object. |
| [ClientViews](../PartDocument/PartDocument_ClientViews.md) | Returns document's client views. |
| [Compacted](../PartDocument/PartDocument_Compacted.md) | Gets the Boolean that states whether this file has been processed for compaction since the last save. |
| [ComponentDefinition](../PartDocument/PartDocument_ComponentDefinition.md) | Gets the primary ComponentDefinition that resides in this file (housing the BRep and its geometric Feature Constraints). |
| [DatabaseRevisionId](../PartDocument/PartDocument_DatabaseRevisionId.md) | Gets the GUID that represents the last saved revision of database contained in this document. This revision id tracks modifications to the database (such as reference changes, geometry changes, etc.) but does not track file property changes. |
| [DefaultCommand](../PartDocument/PartDocument_DefaultCommand.md) | Gets the default command for this document. |
| [Dirty](../PartDocument/PartDocument_Dirty.md) | Gets/Sets a Boolean flag indicating if the Document has been written into, since opened. |
| [DisabledCommandList](../PartDocument/PartDocument_DisabledCommandList.md) | Property that returns the DisabledCommandList object. This object allows the document to disable specific commands. This list contains commands that are disabled in addition to those specified by the DisabledCommandTypes property. |
| [DisabledCommandTypes](../PartDocument/PartDocument_DisabledCommandTypes.md) | Bit mask indicating the disabled command types. |
| [DisplayName](../PartDocument/PartDocument_DisplayName.md) | Gets/Sets the user-displayable name of this Document. Defaults to file-name. |
| [DisplayNameOverridden](../PartDocument/PartDocument_DisplayNameOverridden.md) | Read-write property that gets and sets whether the display name of the document has been overridden. |
| [DisplaySettings](../PartDocument/PartDocument_DisplaySettings.md) | Property that returns the DisplaySettings object. The DisplaySettings object provides access to various display appearance related document settings. |
| [DocumentEvents](../PartDocument/PartDocument_DocumentEvents.md) | This object supports a set of events that are specific to the document. |
| [DocumentInterests](../PartDocument/PartDocument_DocumentInterests.md) | Property that returns the DocumentInterests collection object. |
| [DocumentSubType](../PartDocument/PartDocument_DocumentSubType.md) | Property that returns the subtype of the document. |
| [DocumentType](../PartDocument/PartDocument_DocumentType.md) | Gets the constant that indicates the type of this document. |
| [EmbeddingDocument](../PartDocument/PartDocument_EmbeddingDocument.md) | Read-only property that returns the document in which this document is embedded in. This returns Nothing if the IsEmbeddedDocument is False. |
| [EnvironmentManager](../PartDocument/PartDocument_EnvironmentManager.md) | Property that returns the EnvironmentManager object. |
| [File](../PartDocument/PartDocument_File.md) | Property that returns the file (storage) on disk that contains this document. |
| [FilePropertySets](../PartDocument/PartDocument_FilePropertySets.md) | Read-only property that returns the file PropertySets. This is equivalent to the iProperties that got from Shell Extension. |
| [FileSaveCounter](../PartDocument/PartDocument_FileSaveCounter.md) | Gets the number that indicates the number of times the file has been saved. |
| [FlatPatternSettings](../PartDocument/PartDocument_FlatPatternSettings.md) | Gets the FlatPatternSettings object. |
| [FullDocumentName](../PartDocument/PartDocument_FullDocumentName.md) | Property that returns the fully qualified name of the document. The string is the full file name concatenated with the document name and is a unique identifier for the document. The document name is returned by the Name property on the Document object. |
| [FullFileName](../PartDocument/PartDocument_FullFileName.md) | Gets/Sets the fully qualified file-name of this Document. |
| [GraphicsDataSetsCollection](../PartDocument/PartDocument_GraphicsDataSetsCollection.md) | Property that returns the object for the document. |
| [HasReferencesMissing](../PartDocument/PartDocument_HasReferencesMissing.md) | Read-only property that returns whether there are references missing for this document. |
| [InternalName](../PartDocument/PartDocument_InternalName.md) | Gets the Internal Name (a GUID) for this document. |
| [IsEmbeddedDocument](../PartDocument/PartDocument_IsEmbeddedDocument.md) | Read-only property that returns whether this document is embedded into another document. |
| [IsModifiable](../PartDocument/PartDocument_IsModifiable.md) | Property that returns whether this document can be currently modified. One of the reasons a document may be non-modifiable is if any other document belonging to the file containing this document is currently being edited. |
| [IsSubstitutePart](../PartDocument/PartDocument_IsSubstitutePart.md) | Read-write property that gets and sets whether this part is intended to be used as a substitute part. |
| [LightingStyles](../PartDocument/PartDocument_LightingStyles.md) | Property that returns the LightingStyles collection object. |
| [MarkStyles](../PartDocument/PartDocument_MarkStyles.md) | Get the document's mark styles. |
| [MaterialAssets](../PartDocument/PartDocument_MaterialAssets.md) | Gets Assets collection object that contains the materials associated with the document. |
| [ModelingSettings](../PartDocument/PartDocument_ModelingSettings.md) | Property that returns the ModelingSettings object. The ModelingSettings object provides access to various modeling related document options. This is somewhat equivalent to the Modeling tab of the Document Settings dialog. |
| [ModelStateName](../PartDocument/PartDocument_ModelStateName.md) | Read-only property that returns the model state that this document represents. |
| [NeedsMigrating](../PartDocument/PartDocument_NeedsMigrating.md) | Property that returns whether the document needs to be migrated to the current release. |
| [NonTransactingClientGraphicsCollection](../PartDocument/PartDocument_NonTransactingClientGraphicsCollection.md) | Read-only property that returns the non-transacting ClientGraphicsCollection object. |
| [NonTransactingGraphicsDataSetsCollection](../PartDocument/PartDocument_NonTransactingGraphicsDataSetsCollection.md) | Read-only property that returns the non-transacting GraphicsDataSetsCollection object. |
| [ObjectVisibility](../PartDocument/PartDocument_ObjectVisibility.md) | Property that returns the ObjectVisibility object providing override visibility controls for objects in the document. Changes are not saved with the document. |
| [Open](../PartDocument/PartDocument_Open.md) | Property that returns whether this document is currently open. If False, the document has only been initialized and calling methods or properties on the document could cause it to open. |
| [Parent](../PartDocument/PartDocument_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [PhysicalAssets](../PartDocument/PartDocument_PhysicalAssets.md) | Get AssetsEnumerator object that contains the physical properties associated with the document. |
| [PrintManager](../PartDocument/PartDocument_PrintManager.md) | Property that returns the PrintManager, or when called from a DrawingDocument it returns a DrawingPrintManager object. |
| [PropertySets](../PartDocument/PartDocument_PropertySets.md) | Gets the Property Sets object that controls the file's published-format properties. |
| [RecentChanges](../PartDocument/PartDocument_RecentChanges.md) | Gets a bit-encoded value where the bits indicate the kind of changes made to the document since it became dirty. |
| [ReferencedDocumentDescriptors](../PartDocument/PartDocument_ReferencedDocumentDescriptors.md) | Property that returns an enumeration of descriptors that represent the native document references held by this document. |
| [ReferencedDocuments](../PartDocument/PartDocument_ReferencedDocuments.md) | Property that returns all the documents directly referenced by this document. |
| [ReferencedOLEFileDescriptors](../PartDocument/PartDocument_ReferencedOLEFileDescriptors.md) | Property that returns the collection of linked and embedded files in the document. |
| [ReferencedOLEFileDescriptors2](../PartDocument/PartDocument_ReferencedOLEFileDescriptors2.md) | Gets the collection of OLE attachments made in this Document that match the input type. Returns all OLE attachments if type is kOLEDocumentUnknownObject. |
| [ReferencedOpaqueFileDescriptors](../PartDocument/PartDocument_ReferencedOpaqueFileDescriptors.md) | Gets the collection of descriptor objects, presenting (editable) information about opaque references held. |
| [ReferenceKeyManager](../PartDocument/PartDocument_ReferenceKeyManager.md) | Gets this document's ReferenceKeyManager. |
| [ReferencingDocuments](../PartDocument/PartDocument_ReferencingDocuments.md) | Property that returns all the documents in memory that reference this document. A referencing document may or may not be fully open (i.e. may just be initialized). |
| [RequiresUpdate](../PartDocument/PartDocument_RequiresUpdate.md) | Gets the Boolean indicating if any of the entities within this document's scope is out of date with respect to their driving entities. |
| [ReservedForWrite](../PartDocument/PartDocument_ReservedForWrite.md) | Gets the Boolean flag indicating whether this file has been reserved for write by someone. |
| [ReservedForWriteByMe](../PartDocument/PartDocument_ReservedForWriteByMe.md) | Gets/Sets the Boolean flag indicating whether this file has been reserved for write by the caller. |
| [ReservedForWriteLogin](../PartDocument/PartDocument_ReservedForWriteLogin.md) | Gets the login of the person who currently holds the reservation to write. |
| [ReservedForWriteName](../PartDocument/PartDocument_ReservedForWriteName.md) | Gets the name of the person who currently holds the reservation to write. |
| [ReservedForWriteTime](../PartDocument/PartDocument_ReservedForWriteTime.md) | Gets the time at which the reservation was made. |
| [ReservedForWriteVersion](../PartDocument/PartDocument_ReservedForWriteVersion.md) | Gets the version within this file that has been reserved for write. |
| [SelectionPreferences](../PartDocument/PartDocument_SelectionPreferences.md) | Gets the SelectionPreferences. |
| [SelectionPriority](../PartDocument/PartDocument_SelectionPriority.md) | Gets and sets the current selection priority for the document. |
| [SelectSet](../PartDocument/PartDocument_SelectSet.md) | Property that returns the SelectSet object. |
| [Sketch3DSettings](../PartDocument/PartDocument_Sketch3DSettings.md) | Property that returns the Sketch3DSettings object. The Sketch3DSettings object provides access to various 3D sketch related document options. This is somewhat equivalent to the 3D sketch related properties on Sketch tab of the Document Settings dialog. |
| [SketchActive](../PartDocument/PartDocument_SketchActive.md) | Gets a Boolean flag indicating whether sketching is currently active. |
| [SketchSettings](../PartDocument/PartDocument_SketchSettings.md) | Property that returns the SketchSettings object. The SketchSettings object provides access to various sketch related document options. This is somewhat equivalent to the Sketch tab of the Document Settings dialog. |
| [SoftwareVersionCreated](../PartDocument/PartDocument_SoftwareVersionCreated.md) | Gets the object that encapsulates the version of the software with which this document was first created. |
| [SoftwareVersionSaved](../PartDocument/PartDocument_SoftwareVersionSaved.md) | Gets the object that encapsulates the version of the software with which this document was last saved. |
| [SubType](../PartDocument/PartDocument_SubType.md) | Gets/Sets the sub-Type (a published GUID. See DocCLSIDs.h) of this Document. Setting a new sub-Type will invoke a validation sequence and may fail if the operation is invalid. |
| [TextStyles](../PartDocument/PartDocument_TextStyles.md) | Gets the TextStylesEnumerator object. |
| [Thumbnail](../PartDocument/PartDocument_Thumbnail.md) | Property that returns a bitmap picture of the document. |
| [ThumbnailSaveOption](../PartDocument/PartDocument_ThumbnailSaveOption.md) | Property that returns the current thumbnail (preview picture) save option. |
| [Type](../PartDocument/PartDocument_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitsOfMeasure](../PartDocument/PartDocument_UnitsOfMeasure.md) | Property that returns the UnitsOfMeasure object. |
| [VBAProject](../PartDocument/PartDocument_VBAProject.md) | Property that returns the Autodesk Inventor VBA project for this document. |
| [Views](../PartDocument/PartDocument_Views.md) | Gets all the open views of this document in a collection. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [Navigation between browser and data](../../sample-programs/BrowserPanes_GetNativeBrowserNodeDefinition_Sample.md) | This sample demonstrates the navigation between a browser node and it's corresponding data model object and vice versa. This sample creates a work plane, finds its browser node and gets the work plane object back from the browser node. |

## Version

Introduced in version 4
