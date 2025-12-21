# AssemblyDocument Object

Derived from: [Document](../Document/Document.md) Object

## Description

The AssemblyDocument object represents an in-memory Inventor assembly document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../AssemblyDocument/AssemblyDocument_Activate.md) | Makes this document the active one (receives user-focus). |
| [Close](../AssemblyDocument/AssemblyDocument_Close.md) | Closes this document. |
| [CreateHighlightSet](../AssemblyDocument/AssemblyDocument_CreateHighlightSet.md) | Method that creates a new highlight set. |
| [FindWhereUsed](../AssemblyDocument/AssemblyDocument_FindWhereUsed.md) | Method that obtains the set of documents that reference the given file within this document. |
| [GetLocationFoundIn](../AssemblyDocument/AssemblyDocument_GetLocationFoundIn.md) | Obtains the name of the location this file was found in. |
| [GetMissingAddInBehavior](../AssemblyDocument/AssemblyDocument_GetMissingAddInBehavior.md) | Method that gets the commands disabled when a particular AddIn is absent. |
| [GetPrivateStorage](../AssemblyDocument/AssemblyDocument_GetPrivateStorage.md) | Obtains a private sub-storage within this document with the given name. Can create one, if one does not exist. |
| [GetPrivateStream](../AssemblyDocument/AssemblyDocument_GetPrivateStream.md) | Obtains a private stream within this document with the given name. Can create one, if one does not exist. |
| [GetSelectedObject](../AssemblyDocument/AssemblyDocument_GetSelectedObject.md) | In order to provide better handling of system resources Inventor does not load all of the data when a document is opened but delays loading information until it is needed. A common need in many programs is to have the user select vertices on parts. Instead of loading the part model in order to return the true selected Vertex, Inventor returns a GenericObject. You can use this method to obtain more information about the selected object. If it is a vertex you can get the point coordinates without forcing the entire model to be loaded, or if you do need to do additional processing that requires access to the full model you can also force that by using the "SelectedObject" argument. |
| [HasPrivateStorage](../AssemblyDocument/AssemblyDocument_HasPrivateStorage.md) | Obtains a Boolean flag indicating if the specified sub-storage exists within this document. |
| [HasPrivateStream](../AssemblyDocument/AssemblyDocument_HasPrivateStream.md) | Obtains a Boolean flag indicating if the specified stream exists within this document. |
| [PutInternalNameAndRevisionId](../AssemblyDocument/AssemblyDocument_PutInternalNameAndRevisionId.md) | Constructs and sets the Internal Name and Revision Identifier for this Document from strings supplied. This can only be done on a previously un-saved document (New or SaveCopyAs) |
| [Rebuild](../AssemblyDocument/AssemblyDocument_Rebuild.md) | Performs compute operations on all of the entities within this document's scope as if all of the driving entities had been 'dirtied.' |
| [Rebuild2](../AssemblyDocument/AssemblyDocument_Rebuild2.md) | Method that performs compute operations on all of the entities within this Document's scope as if all of the driving entities had been 'dirtied'. |
| [ReleaseReference](../AssemblyDocument/AssemblyDocument_ReleaseReference.md) | Method that releases the reference that gets added if a document is opened invisibly through the API. Releasing the reference on a hidden document makes it a candidate for closure the next time Inventor closes all unreferenced documents. |
| [ResolveFile](../AssemblyDocument/AssemblyDocument_ResolveFile.md) | Method that invoke the resolve file for the document if there are references missing. |
| [RevertReservedForWriteByMe](../AssemblyDocument/AssemblyDocument_RevertReservedForWriteByMe.md) | Method that reverts the file checked out by the caller. |
| [Save](../AssemblyDocument/AssemblyDocument_Save.md) | Saves this document to disk. |
| [Save2](../AssemblyDocument/AssemblyDocument_Save2.md) | Method that saves the document and the specified dependent documents. |
| [SaveAs](../AssemblyDocument/AssemblyDocument_SaveAs.md) | Saves this document into a file of the specified name. |
| [SaveAs2](../AssemblyDocument/AssemblyDocument_SaveAs2.md) | Saves this document into a file of the specified name. |
| [SetMissingAddInBehavior](../AssemblyDocument/AssemblyDocument_SetMissingAddInBehavior.md) | Method that sets the commands to be disabled when a particular AddIn is absent. |
| [SetThumbnailSaveOption](../AssemblyDocument/AssemblyDocument_SetThumbnailSaveOption.md) | Method that sets the thumbnail (preview picture) save option. |
| [Update](../AssemblyDocument/AssemblyDocument_Update.md) | Performs compute operations on all of the entities within this Document's scope that may be out of date with respect to their driving entities. |
| [Update2](../AssemblyDocument/AssemblyDocument_Update2.md) | Method that performs compute operations on all of the entities within this Document's scope that may be out of date with respect to their driving entities. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActivatedObject](../AssemblyDocument/AssemblyDocument_ActivatedObject.md) | Gets the object that has been in-place activated for edit within the context of this document. |
| [ActiveLightingStyle](../AssemblyDocument/AssemblyDocument_ActiveLightingStyle.md) | Gets the active lighting style object. |
| [AllReferencedDocuments](../AssemblyDocument/AssemblyDocument_AllReferencedDocuments.md) | Property that returns all the document references of this Document along with all of the recursively nested references. |
| [AppearanceAssets](../AssemblyDocument/AssemblyDocument_AppearanceAssets.md) | Read-only property that returns an AssetsEnumerator collection object that contains the appearances associated with the document. |
| [Assets](../AssemblyDocument/AssemblyDocument_Assets.md) | Get Assets collection object that contains all of the assets, regardless of type, that are associated with the document. |
| [AssociativeForeignFilename](../AssemblyDocument/AssemblyDocument_AssociativeForeignFilename.md) | Read-only property that returns the full file name of the associative foreign file. This property returns empty string if the IsEmbeddedDocument returns False. |
| [AttributeManager](../AssemblyDocument/AssemblyDocument_AttributeManager.md) | Returns the AttributeManager object. |
| [AttributeSets](../AssemblyDocument/AssemblyDocument_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BrowserPanes](../AssemblyDocument/AssemblyDocument_BrowserPanes.md) | Property that returns the  collection object. |
| [ClientViews](../AssemblyDocument/AssemblyDocument_ClientViews.md) | Returns document's client views. |
| [Compacted](../AssemblyDocument/AssemblyDocument_Compacted.md) | Gets the Boolean that states whether this file has been processed for compaction since the last save. |
| [ComponentDefinition](../AssemblyDocument/AssemblyDocument_ComponentDefinition.md) | Property that returns the object associated with this assembly. For a standard assembly document, an AssemblyComponentDefinition object will be returned. For a weldment assembly, a Weldment object. |
| [DatabaseRevisionId](../AssemblyDocument/AssemblyDocument_DatabaseRevisionId.md) | Gets the GUID that represents the last saved revision of database contained in this document. This revision id tracks modifications to the database (such as reference changes, geometry changes, etc.) but does not track file property changes. |
| [DefaultCommand](../AssemblyDocument/AssemblyDocument_DefaultCommand.md) | Gets the default command for this document. |
| [DesignViewInfo](../AssemblyDocument/AssemblyDocument_DesignViewInfo.md) | Gets the design view information for the document as a String containing XML formatted data. For more information on this XML format see [More XML Design View Info...](MoreXMLDesignViewInfo_Overview.md) |
| [Dirty](../AssemblyDocument/AssemblyDocument_Dirty.md) | Gets/Sets a Boolean flag indicating if the Document has been written into, since opened. |
| [DisabledCommandList](../AssemblyDocument/AssemblyDocument_DisabledCommandList.md) | Property that returns the DisabledCommandList object. This object allows the document to disable specific commands. This list contains commands that are disabled in addition to those specified by the DisabledCommandTypes property. |
| [DisabledCommandTypes](../AssemblyDocument/AssemblyDocument_DisabledCommandTypes.md) | Bit mask indicating the disabled command types. |
| [DisplayName](../AssemblyDocument/AssemblyDocument_DisplayName.md) | Gets/Sets the user-displayable name of this Document. Defaults to file-name. |
| [DisplayNameOverridden](../AssemblyDocument/AssemblyDocument_DisplayNameOverridden.md) | Read-write property that gets and sets whether the display name of the document has been overridden. |
| [DisplaySettings](../AssemblyDocument/AssemblyDocument_DisplaySettings.md) | Property that returns the DisplaySettings object. The DisplaySettings object provides access to various display appearance related document settings. |
| [DocumentEvents](../AssemblyDocument/AssemblyDocument_DocumentEvents.md) | This object supports a set of events that are specific to the document. |
| [DocumentInterests](../AssemblyDocument/AssemblyDocument_DocumentInterests.md) | Property that returns the DocumentInterests collection object. |
| [DocumentSubType](../AssemblyDocument/AssemblyDocument_DocumentSubType.md) | Property that returns the subtype of the document. |
| [DocumentType](../AssemblyDocument/AssemblyDocument_DocumentType.md) | Gets the constant that indicates the type of this document. |
| [EmbeddingDocument](../AssemblyDocument/AssemblyDocument_EmbeddingDocument.md) | Read-only property that returns the document in which this document is embedded in. This returns Nothing if the IsEmbeddedDocument is False. |
| [EnvironmentManager](../AssemblyDocument/AssemblyDocument_EnvironmentManager.md) | Property that returns the EnvironmentManager object. |
| [File](../AssemblyDocument/AssemblyDocument_File.md) | Property that returns the file (storage) on disk that contains this document. |
| [FilePropertySets](../AssemblyDocument/AssemblyDocument_FilePropertySets.md) | Read-only property that returns the file PropertySets. This is equivalent to the iProperties that got from Shell Extension. |
| [FileSaveCounter](../AssemblyDocument/AssemblyDocument_FileSaveCounter.md) | Gets the number that indicates the number of times the file has been saved. |
| [FullDocumentName](../AssemblyDocument/AssemblyDocument_FullDocumentName.md) | Property that returns the fully qualified name of the document. The string is the full file name concatenated with the document name and is a unique identifier for the document. The document name is returned by the Name property on the Document object. |
| [FullFileName](../AssemblyDocument/AssemblyDocument_FullFileName.md) | Gets/Sets the fully qualified file-name of this Document. |
| [GraphicsDataSetsCollection](../AssemblyDocument/AssemblyDocument_GraphicsDataSetsCollection.md) | Property that returns the object for the document. |
| [HasReferencesMissing](../AssemblyDocument/AssemblyDocument_HasReferencesMissing.md) | Read-only property that returns whether there are references missing for this document. |
| [InternalName](../AssemblyDocument/AssemblyDocument_InternalName.md) | Gets the Internal Name (a GUID) for this document. |
| [IsEmbeddedDocument](../AssemblyDocument/AssemblyDocument_IsEmbeddedDocument.md) | Read-only property that returns whether this document is embedded into another document. |
| [IsModifiable](../AssemblyDocument/AssemblyDocument_IsModifiable.md) | Property that returns whether this document can be currently modified. One of the reasons a document may be non-modifiable is if any other document belonging to the file containing this document is currently being edited. |
| [IsOpenExpress](../AssemblyDocument/AssemblyDocument_IsOpenExpress.md) | Read-write property that gets and sets a Boolean flag indicating whether this assembly is currently open in Express mode. When set this property it can only be set from True to False to load the document into full mode. To switch the document from full mode to express mode users should close it and re-open it in express mode using OpenWithOptions method. |
| [LightingStyles](../AssemblyDocument/AssemblyDocument_LightingStyles.md) | Property that returns the LightingStyles collection object. |
| [MaterialAssets](../AssemblyDocument/AssemblyDocument_MaterialAssets.md) | Get AssetsEnumerator object that contains the materials associated with the document. |
| [ModelingSettings](../AssemblyDocument/AssemblyDocument_ModelingSettings.md) | Property that returns the ModelingSettings object. The ModelingSettings object provides access to various modeling related document options. This is somewhat equivalent to the Modeling tab of the Document Settings dialog. |
| [ModelStateName](../AssemblyDocument/AssemblyDocument_ModelStateName.md) | Read-only property that returns the model state that this document represents. |
| [NeedsMigrating](../AssemblyDocument/AssemblyDocument_NeedsMigrating.md) | Property that returns whether the document needs to be migrated to the current release. |
| [NonTransactingClientGraphicsCollection](../AssemblyDocument/AssemblyDocument_NonTransactingClientGraphicsCollection.md) | Read-only property that returns the non-transacting ClientGraphicsCollection object. |
| [NonTransactingGraphicsDataSetsCollection](../AssemblyDocument/AssemblyDocument_NonTransactingGraphicsDataSetsCollection.md) | Read-only property that returns the non-transacting GraphicsDataSetsCollection object. |
| [ObjectVisibility](../AssemblyDocument/AssemblyDocument_ObjectVisibility.md) | Property that returns the ObjectVisibility object providing override visibility controls for objects in the document. Changes are not saved with the document. |
| [Open](../AssemblyDocument/AssemblyDocument_Open.md) | Property that returns whether this document is currently open. If False, the document has only been initialized and calling methods or properties on the document could cause it to open. |
| [Parent](../AssemblyDocument/AssemblyDocument_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [PhysicalAssets](../AssemblyDocument/AssemblyDocument_PhysicalAssets.md) | Get AssetsEnumerator object that contains the physical properties associated with the document. |
| [PrintManager](../AssemblyDocument/AssemblyDocument_PrintManager.md) | Property that returns the PrintManager, or when called from a DrawingDocument it returns a DrawingPrintManager object. |
| [PropertySets](../AssemblyDocument/AssemblyDocument_PropertySets.md) | Gets the Property Sets object that controls the file's published-format properties. |
| [RecentChanges](../AssemblyDocument/AssemblyDocument_RecentChanges.md) | Gets a bit-encoded value where the bits indicate the kind of changes made to the document since it became dirty. |
| [ReferencedDocumentDescriptors](../AssemblyDocument/AssemblyDocument_ReferencedDocumentDescriptors.md) | Property that returns an enumeration of descriptors that represent the native document references held by this document. |
| [ReferencedDocuments](../AssemblyDocument/AssemblyDocument_ReferencedDocuments.md) | Property that returns all the documents directly referenced by this document. |
| [ReferencedOLEFileDescriptors](../AssemblyDocument/AssemblyDocument_ReferencedOLEFileDescriptors.md) | Property that returns the collection of linked and embedded files in the document. |
| [ReferencedOLEFileDescriptors2](../AssemblyDocument/AssemblyDocument_ReferencedOLEFileDescriptors2.md) | Gets the collection of OLE attachments made in this Document that match the input type. Returns all OLE attachments if type is kOLEDocumentUnknownObject. |
| [ReferencedOpaqueFileDescriptors](../AssemblyDocument/AssemblyDocument_ReferencedOpaqueFileDescriptors.md) | Gets the collection of descriptor objects, presenting (editable) information about opaque references held. |
| [ReferenceKeyManager](../AssemblyDocument/AssemblyDocument_ReferenceKeyManager.md) | Gets this document's ReferenceKeyManager. |
| [ReferencingDocuments](../AssemblyDocument/AssemblyDocument_ReferencingDocuments.md) | Property that returns all the documents in memory that reference this document. A referencing document may or may not be fully open (i.e. may just be initialized). |
| [RequiresUpdate](../AssemblyDocument/AssemblyDocument_RequiresUpdate.md) | Gets the Boolean indicating if any of the entities within this document's scope is out of date with respect to their driving entities. |
| [ReservedForWrite](../AssemblyDocument/AssemblyDocument_ReservedForWrite.md) | Gets the Boolean flag indicating whether this file has been reserved for write by someone. |
| [ReservedForWriteByMe](../AssemblyDocument/AssemblyDocument_ReservedForWriteByMe.md) | Gets/Sets the Boolean flag indicating whether this file has been reserved for write by the caller. |
| [ReservedForWriteLogin](../AssemblyDocument/AssemblyDocument_ReservedForWriteLogin.md) | Gets the login of the person who currently holds the reservation to write. |
| [ReservedForWriteName](../AssemblyDocument/AssemblyDocument_ReservedForWriteName.md) | Gets the name of the person who currently holds the reservation to write. |
| [ReservedForWriteTime](../AssemblyDocument/AssemblyDocument_ReservedForWriteTime.md) | Gets the time at which the reservation was made. |
| [ReservedForWriteVersion](../AssemblyDocument/AssemblyDocument_ReservedForWriteVersion.md) | Gets the version within this file that has been reserved for write. |
| [SelectionPreferences](../AssemblyDocument/AssemblyDocument_SelectionPreferences.md) | Gets the SelectionPreferences. |
| [SelectionPriority](../AssemblyDocument/AssemblyDocument_SelectionPriority.md) | Gets and sets the current selection priority for the document. |
| [SelectSet](../AssemblyDocument/AssemblyDocument_SelectSet.md) | Property that returns the SelectSet object. |
| [SketchSettings](../AssemblyDocument/AssemblyDocument_SketchSettings.md) | Property that returns the SketchSettings object. The SketchSettings object provides access to various sketch related document options. This is somewhat equivalent to the Sketch tab of the Document Settings dialog. |
| [SoftwareVersionCreated](../AssemblyDocument/AssemblyDocument_SoftwareVersionCreated.md) | Gets the object that encapsulates the version of the software with which this document was first created. |
| [SoftwareVersionSaved](../AssemblyDocument/AssemblyDocument_SoftwareVersionSaved.md) | Gets the object that encapsulates the version of the software with which this document was last saved. |
| [SubType](../AssemblyDocument/AssemblyDocument_SubType.md) | Gets/Sets the sub-Type (a published GUID. See DocCLSIDs.h) of this Document. Setting a new sub-Type will invoke a validation sequence and may fail if the operation is invalid. |
| [TextStyles](../AssemblyDocument/AssemblyDocument_TextStyles.md) | Gets the TextStylesEnumerator object. |
| [Thumbnail](../AssemblyDocument/AssemblyDocument_Thumbnail.md) | Property that returns a bitmap picture of the document. |
| [ThumbnailSaveOption](../AssemblyDocument/AssemblyDocument_ThumbnailSaveOption.md) | Property that returns the current thumbnail (preview picture) save option. |
| [Type](../AssemblyDocument/AssemblyDocument_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitsOfMeasure](../AssemblyDocument/AssemblyDocument_UnitsOfMeasure.md) | Property that returns the UnitsOfMeasure object. |
| [VBAProject](../AssemblyDocument/AssemblyDocument_VBAProject.md) | Property that returns the Autodesk Inventor VBA project for this document. |
| [Views](../AssemblyDocument/AssemblyDocument_Views.md) | Gets all the open views of this document in a collection. |

## Accessed From

[AssemblyComponentDefinition.Parent](../AssemblyComponentDefinition/AssemblyComponentDefinition_Parent.md), [AssemblyComponentDefinitions.Parent](../AssemblyComponentDefinitions/AssemblyComponentDefinitions_Parent.md), [WeldmentComponentDefinition.Parent](../WeldmentComponentDefinition/WeldmentComponentDefinition_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iAssembly occurrences](../../sample-programs/AddiAssemblyMember_Sample.md) | This sample demonstrates adding iAssembly occurrences to an assembly. |
| [Traverse an Assembly](../../sample-programs/AssemblyTraverse_Sample.md) | This sample shows how to recursively traverse an assembly and get the count of leaf node components and subassemblies. |
| [Using the BOM APIs](../../sample-programs/BOM_Sample.md) | This sample demonstrates the Bill of Materials API functionality in assemblies. |
| [Exporting the assembly BOM](../../sample-programs/BOMView_Export_Sample.md) | This sample demonstrates exporting the Assembly BOM to an external file. |
| [Replace content center part](../../sample-programs/ContentCenterPartReplace_Sample.md) | This sample demonstrates how to replace the content part referenced by an assembly occurrence. |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [Export to IFC Format Sample](../../sample-programs/ExportToIFCFormatSample_Sample.md) | This sample demonstrates how to export an assembly to IFC format. |

## Version

Introduced in version 4
