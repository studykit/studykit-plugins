# DrawingDocument Object

Derived from: [Document](../Document/Document.md) Object

## Description

The DrawingDocument object provides methods and properties to create, activate, save, and query many properties of individual drawing documents.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../DrawingDocument/DrawingDocument_Activate.md) | Makes this document the active one (receives user-focus). |
| [Close](../DrawingDocument/DrawingDocument_Close.md) | Closes this document. |
| [CreateHighlightSet](../DrawingDocument/DrawingDocument_CreateHighlightSet.md) | Method that creates a new highlight set. |
| [FindWhereUsed](../DrawingDocument/DrawingDocument_FindWhereUsed.md) | Method that obtains the set of documents that reference the given file within this document. |
| [GetLocationFoundIn](../DrawingDocument/DrawingDocument_GetLocationFoundIn.md) | Obtains the name of the location this file was found in. |
| [GetMissingAddInBehavior](../DrawingDocument/DrawingDocument_GetMissingAddInBehavior.md) | Method that gets the commands disabled when a particular AddIn is absent. |
| [GetPrivateStorage](../DrawingDocument/DrawingDocument_GetPrivateStorage.md) | Obtains a private sub-storage within this document with the given name. Can create one, if one does not exist. |
| [GetPrivateStream](../DrawingDocument/DrawingDocument_GetPrivateStream.md) | Obtains a private stream within this document with the given name. Can create one, if one does not exist. |
| [HasPrivateStorage](../DrawingDocument/DrawingDocument_HasPrivateStorage.md) | Obtains a Boolean flag indicating if the specified sub-storage exists within this document. |
| [HasPrivateStream](../DrawingDocument/DrawingDocument_HasPrivateStream.md) | Obtains a Boolean flag indicating if the specified stream exists within this document. |
| [MakeAllViewsPrecise](../DrawingDocument/DrawingDocument_MakeAllViewsPrecise.md) | Set all drawing views in the document to be precise views. |
| [MakeAllViewsRaster](../DrawingDocument/DrawingDocument_MakeAllViewsRaster.md) | Set all drawing views in the document to be raster views. |
| [ProcessViewSelection](../DrawingDocument/DrawingDocument_ProcessViewSelection.md) | Process object selection according to the context of the document referenced by the containing view. |
| [PutInternalNameAndRevisionId](../DrawingDocument/DrawingDocument_PutInternalNameAndRevisionId.md) | Constructs and sets the Internal Name and Revision Identifier for this Document from strings supplied. This can only be done on a previously un-saved document (New or SaveCopyAs) |
| [Rebuild](../DrawingDocument/DrawingDocument_Rebuild.md) | Performs compute operations on all of the entities within this document's scope as if all of the driving entities had been 'dirtied.' |
| [Rebuild2](../DrawingDocument/DrawingDocument_Rebuild2.md) | Method that performs compute operations on all of the entities within this Document's scope as if all of the driving entities had been 'dirtied'. |
| [ReleaseReference](../DrawingDocument/DrawingDocument_ReleaseReference.md) | Method that releases the reference that gets added if a document is opened invisibly through the API. Releasing the reference on a hidden document makes it a candidate for closure the next time Inventor closes all unreferenced documents. |
| [ResolveFile](../DrawingDocument/DrawingDocument_ResolveFile.md) | Method that invoke the resolve file for the document if there are references missing. |
| [RevertReservedForWriteByMe](../DrawingDocument/DrawingDocument_RevertReservedForWriteByMe.md) | Method that reverts the file checked out by the caller. |
| [Save](../DrawingDocument/DrawingDocument_Save.md) | Saves this document to disk. |
| [Save2](../DrawingDocument/DrawingDocument_Save2.md) | Method that saves the document and the specified dependent documents. |
| [SaveAs](../DrawingDocument/DrawingDocument_SaveAs.md) | Saves this document into a file of the specified name. |
| [SaveAs2](../DrawingDocument/DrawingDocument_SaveAs2.md) | Saves this document into a file of the specified name. |
| [SaveAsInventorDWG](../DrawingDocument/DrawingDocument_SaveAsInventorDWG.md) | Method that saves the document as an Inventor DWG with the specified name. |
| [SetMissingAddInBehavior](../DrawingDocument/DrawingDocument_SetMissingAddInBehavior.md) | Method that sets the commands to be disabled when a particular AddIn is absent. |
| [SetThumbnailSaveOption](../DrawingDocument/DrawingDocument_SetThumbnailSaveOption.md) | Method that sets the thumbnail (preview picture) save option. |
| [Update](../DrawingDocument/DrawingDocument_Update.md) | Performs compute operations on all of the entities within this Document's scope that may be out of date with respect to their driving entities. |
| [Update2](../DrawingDocument/DrawingDocument_Update2.md) | Method that performs compute operations on all of the entities within this Document's scope that may be out of date with respect to their driving entities. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActivatedObject](../DrawingDocument/DrawingDocument_ActivatedObject.md) | Gets the object that has been in-place activated for edit within the context of this document. |
| [ActiveSheet](../DrawingDocument/DrawingDocument_ActiveSheet.md) | Property that returns the currently active sheet. |
| [AllReferencedDocuments](../DrawingDocument/DrawingDocument_AllReferencedDocuments.md) | Property that returns all the document references of this Document along with all of the recursively nested references. |
| [AttributeManager](../DrawingDocument/DrawingDocument_AttributeManager.md) | Returns the AttributeManager object. |
| [AttributeSets](../DrawingDocument/DrawingDocument_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AutoCADBlockDefinitions](../DrawingDocument/DrawingDocument_AutoCADBlockDefinitions.md) | Property that returns the AutoCADBlockDefinitions collection object. |
| [BorderDefinitions](../DrawingDocument/DrawingDocument_BorderDefinitions.md) | Property that returns the BorderDefinitions collection object. This object provides access to all of the border definitions in the document and provides functionality to create new border definitions. |
| [BrowserPanes](../DrawingDocument/DrawingDocument_BrowserPanes.md) | Property that returns the  collection object. |
| [ClientViews](../DrawingDocument/DrawingDocument_ClientViews.md) | Returns document's client views. |
| [Compacted](../DrawingDocument/DrawingDocument_Compacted.md) | Gets the Boolean that states whether this file has been processed for compaction since the last save. |
| [ContainingDWGDocument](../DrawingDocument/DrawingDocument_ContainingDWGDocument.md) | Gets the reference to the containing DWG document when this document is stored in a DWG. |
| [DatabaseRevisionId](../DrawingDocument/DrawingDocument_DatabaseRevisionId.md) | Gets the GUID that represents the last saved revision of database contained in this document. This revision id tracks modifications to the database (such as reference changes, geometry changes, etc.) but does not track file property changes. |
| [DefaultCommand](../DrawingDocument/DrawingDocument_DefaultCommand.md) | Gets the default command for this document. |
| [Dirty](../DrawingDocument/DrawingDocument_Dirty.md) | Gets/Sets a Boolean flag indicating if the Document has been written into, since opened. |
| [DisabledCommandList](../DrawingDocument/DrawingDocument_DisabledCommandList.md) | Property that returns the DisabledCommandList object. This object allows the document to disable specific commands. This list contains commands that are disabled in addition to those specified by the DisabledCommandTypes property. |
| [DisabledCommandTypes](../DrawingDocument/DrawingDocument_DisabledCommandTypes.md) | Bit mask indicating the disabled command types. |
| [DisplayName](../DrawingDocument/DrawingDocument_DisplayName.md) | Gets/Sets the user-displayable name of this Document. Defaults to file-name. |
| [DisplayNameOverridden](../DrawingDocument/DrawingDocument_DisplayNameOverridden.md) | Read-write property that gets and sets whether the display name of the document has been overridden. |
| [DocumentEvents](../DrawingDocument/DrawingDocument_DocumentEvents.md) | This object supports a set of events that are specific to the document. |
| [DocumentInterests](../DrawingDocument/DrawingDocument_DocumentInterests.md) | Property that returns the DocumentInterests collection object. |
| [DocumentSubType](../DrawingDocument/DrawingDocument_DocumentSubType.md) | Property that returns the subtype of the document. |
| [DocumentType](../DrawingDocument/DrawingDocument_DocumentType.md) | Gets the constant that indicates the type of this document. |
| [DrawingBOMs](../DrawingDocument/DrawingDocument_DrawingBOMs.md) | Property that returns the collection of locally stored BOMs in this drawing document. |
| [DrawingEvents](../DrawingDocument/DrawingDocument_DrawingEvents.md) | Property that gets the DrawingEvents object. This provides drawing event notification such as onRetrieveDimensions. |
| [DrawingHatchPatternsManager](../DrawingDocument/DrawingDocument_DrawingHatchPatternsManager.md) | Read-only property that returns the DrawingHatchPatternsManager object. |
| [DrawingSettings](../DrawingDocument/DrawingDocument_DrawingSettings.md) | The DrawingSettings object provides access to various drawing related document settings. This is somewhat equivalent to the Drawing tab of the Document Settings dialog. |
| [EnvironmentManager](../DrawingDocument/DrawingDocument_EnvironmentManager.md) | Property that returns the EnvironmentManager object. |
| [File](../DrawingDocument/DrawingDocument_File.md) | Property that returns the file (storage) on disk that contains this document. |
| [FilePropertySets](../DrawingDocument/DrawingDocument_FilePropertySets.md) | Read-only property that returns the file PropertySets. This is equivalent to the iProperties that got from Shell Extension. |
| [FileSaveCounter](../DrawingDocument/DrawingDocument_FileSaveCounter.md) | Gets the number that indicates the number of times the file has been saved. |
| [FullDocumentName](../DrawingDocument/DrawingDocument_FullDocumentName.md) | Property that returns the fully qualified name of the document. The string is the full file name concatenated with the document name and is a unique identifier for the document. The document name is returned by the Name property on the Document object. |
| [FullFileName](../DrawingDocument/DrawingDocument_FullFileName.md) | Gets/Sets the fully qualified file-name of this Document. |
| [GraphicsDataSetsCollection](../DrawingDocument/DrawingDocument_GraphicsDataSetsCollection.md) | Property that returns the object for the document. |
| [HasReferencesMissing](../DrawingDocument/DrawingDocument_HasReferencesMissing.md) | Read-only property that returns whether there are references missing for this document. |
| [InternalName](../DrawingDocument/DrawingDocument_InternalName.md) | Gets the Internal Name (a GUID) for this document. |
| [IsInventorDWG](../DrawingDocument/DrawingDocument_IsInventorDWG.md) | Property that returns whether this is an Inventor DWG document. |
| [IsModifiable](../DrawingDocument/DrawingDocument_IsModifiable.md) | Property that returns whether this document can be currently modified. One of the reasons a document may be non-modifiable is if any other document belonging to the file containing this document is currently being edited. |
| [ModelStateName](../DrawingDocument/DrawingDocument_ModelStateName.md) | Read-only property that returns the model state that this document represents. |
| [NeedsMigrating](../DrawingDocument/DrawingDocument_NeedsMigrating.md) | Property that returns whether the document needs to be migrated to the current release. |
| [NonTransactingClientGraphicsCollection](../DrawingDocument/DrawingDocument_NonTransactingClientGraphicsCollection.md) | Read-only property that returns the non-transacting ClientGraphicsCollection object. |
| [NonTransactingGraphicsDataSetsCollection](../DrawingDocument/DrawingDocument_NonTransactingGraphicsDataSetsCollection.md) | Read-only property that returns the non-transacting GraphicsDataSetsCollection object. |
| [Open](../DrawingDocument/DrawingDocument_Open.md) | Property that returns whether this document is currently open. If False, the document has only been initialized and calling methods or properties on the document could cause it to open. |
| [Parameters](../DrawingDocument/DrawingDocument_Parameters.md) | Property that returns the set of parameters stored in this drawing document. |
| [Parent](../DrawingDocument/DrawingDocument_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [PrintManager](../DrawingDocument/DrawingDocument_PrintManager.md) | Property that returns the PrintManager, or when called from a DrawingDocument it returns a DrawingPrintManager object. |
| [PropertySets](../DrawingDocument/DrawingDocument_PropertySets.md) | Gets the Property Sets object that controls the file's published-format properties. |
| [RecentChanges](../DrawingDocument/DrawingDocument_RecentChanges.md) | Gets a bit-encoded value where the bits indicate the kind of changes made to the document since it became dirty. |
| [ReferencedDocumentDescriptors](../DrawingDocument/DrawingDocument_ReferencedDocumentDescriptors.md) | Property that returns an enumeration of descriptors that represent the native document references held by this document. |
| [ReferencedDocuments](../DrawingDocument/DrawingDocument_ReferencedDocuments.md) | Property that returns all the documents directly referenced by this document. |
| [ReferencedOLEFileDescriptors](../DrawingDocument/DrawingDocument_ReferencedOLEFileDescriptors.md) | Property that returns the collection of linked and embedded files in the document. |
| [ReferencedOLEFileDescriptors2](../DrawingDocument/DrawingDocument_ReferencedOLEFileDescriptors2.md) | Gets the collection of OLE attachments made in this Document that match the input type. Returns all OLE attachments if type is kOLEDocumentUnknownObject. |
| [ReferencedOpaqueFileDescriptors](../DrawingDocument/DrawingDocument_ReferencedOpaqueFileDescriptors.md) | Gets the collection of descriptor objects, presenting (editable) information about opaque references held. |
| [ReferenceKeyManager](../DrawingDocument/DrawingDocument_ReferenceKeyManager.md) | Gets this document's ReferenceKeyManager. |
| [ReferencingDocuments](../DrawingDocument/DrawingDocument_ReferencingDocuments.md) | Property that returns all the documents in memory that reference this document. A referencing document may or may not be fully open (i.e. may just be initialized). |
| [RequiresUpdate](../DrawingDocument/DrawingDocument_RequiresUpdate.md) | Gets the Boolean indicating if any of the entities within this document's scope is out of date with respect to their driving entities. |
| [ReservedForWrite](../DrawingDocument/DrawingDocument_ReservedForWrite.md) | Gets the Boolean flag indicating whether this file has been reserved for write by someone. |
| [ReservedForWriteByMe](../DrawingDocument/DrawingDocument_ReservedForWriteByMe.md) | Gets/Sets the Boolean flag indicating whether this file has been reserved for write by the caller. |
| [ReservedForWriteLogin](../DrawingDocument/DrawingDocument_ReservedForWriteLogin.md) | Gets the login of the person who currently holds the reservation to write. |
| [ReservedForWriteName](../DrawingDocument/DrawingDocument_ReservedForWriteName.md) | Gets the name of the person who currently holds the reservation to write. |
| [ReservedForWriteTime](../DrawingDocument/DrawingDocument_ReservedForWriteTime.md) | Gets the time at which the reservation was made. |
| [ReservedForWriteVersion](../DrawingDocument/DrawingDocument_ReservedForWriteVersion.md) | Gets the version within this file that has been reserved for write. |
| [SelectionPreferences](../DrawingDocument/DrawingDocument_SelectionPreferences.md) | Gets the SelectionPreferences. |
| [SelectionPriority](../DrawingDocument/DrawingDocument_SelectionPriority.md) | Gets and sets the current selection priority for the document. |
| [SelectSet](../DrawingDocument/DrawingDocument_SelectSet.md) | Property that returns the SelectSet object. |
| [SheetFormats](../DrawingDocument/DrawingDocument_SheetFormats.md) | Property that returns the SheetFormats collection object. |
| [Sheets](../DrawingDocument/DrawingDocument_Sheets.md) | Property that returns the Sheets collection object. This object provides access to all of the sheets in the document. |
| [SheetSettings](../DrawingDocument/DrawingDocument_SheetSettings.md) | Property that returns the SheetSettings object. The SheetSettings object provides access to various sheet related document options. This is somewhat equivalent to the Sheet tab of the Document Settings dialog. |
| [SketchedSymbolDefinitions](../DrawingDocument/DrawingDocument_SketchedSymbolDefinitions.md) | Property that returns the SketchedSymbolDefinitions collection object. This object provides access to all of the sketched symbol definitions available for placement in the document and provides functionality to create new sketched symbol definitions. |
| [SketchSettings](../DrawingDocument/DrawingDocument_SketchSettings.md) | Property that returns the SketchSettings object. The SketchSettings object provides access to various sketch related document options. This is somewhat equivalent to the Sketch tab of the Document Settings dialog. |
| [SoftwareVersionCreated](../DrawingDocument/DrawingDocument_SoftwareVersionCreated.md) | Gets the object that encapsulates the version of the software with which this document was first created. |
| [SoftwareVersionSaved](../DrawingDocument/DrawingDocument_SoftwareVersionSaved.md) | Gets the object that encapsulates the version of the software with which this document was last saved. |
| [StylesManager](../DrawingDocument/DrawingDocument_StylesManager.md) | Property that returns the DrawingStylesManager object. |
| [SubType](../DrawingDocument/DrawingDocument_SubType.md) | Gets/Sets the sub-Type (a published GUID. See DocCLSIDs.h) of this Document. Setting a new sub-Type will invoke a validation sequence and may fail if the operation is invalid. |
| [Thumbnail](../DrawingDocument/DrawingDocument_Thumbnail.md) | Property that returns a bitmap picture of the document. |
| [ThumbnailSaveOption](../DrawingDocument/DrawingDocument_ThumbnailSaveOption.md) | Property that returns the current thumbnail (preview picture) save option. |
| [TitleBlockDefinitions](../DrawingDocument/DrawingDocument_TitleBlockDefinitions.md) | Property that returns the TitleBlockDefinitions collection object. This object provides access to all of the title block definition in the document and provides functionality to create new title block definitions. |
| [Type](../DrawingDocument/DrawingDocument_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnitsOfMeasure](../DrawingDocument/DrawingDocument_UnitsOfMeasure.md) | Property that returns the UnitsOfMeasure object. |
| [VBAProject](../DrawingDocument/DrawingDocument_VBAProject.md) | Property that returns the Autodesk Inventor VBA project for this document. |
| [Views](../DrawingDocument/DrawingDocument_Views.md) | Gets all the open views of this document in a collection. |

## Accessed From

[AutoCADBlockDefinition.Parent](../AutoCADBlockDefinition/AutoCADBlockDefinition_Parent.md), [BorderDefinition.Parent](../BorderDefinition/BorderDefinition_Parent.md), [DrawingBOM.Parent](../DrawingBOM/DrawingBOM_Parent.md), [DrawingEvents.Parent](../DrawingEvents/DrawingEvents_Parent.md), [DrawingHatchPatternsManager.Parent](../DrawingHatchPatternsManager/DrawingHatchPatternsManager_Parent.md), [DrawingSettings.Parent](../DrawingSettings/DrawingSettings_Parent.md), [DrawingStylesManager.Parent](../DrawingStylesManager/DrawingStylesManager_Parent.md), [SheetFormat.Parent](../SheetFormat/SheetFormat_Parent.md), [SheetSettings.Parent](../SheetSettings/SheetSettings_Parent.md), [SketchedSymbolDefinition.Parent](../SketchedSymbolDefinition/SketchedSymbolDefinition_Parent.md), [TitleBlockDefinition.Parent](../TitleBlockDefinition/TitleBlockDefinition_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Balloons - edit](../../sample-programs/Balloons_Sample.md) | This sample demonstrates the editing of balloons in a drawing. |
| [Creation a balloon](../../sample-programs/Balloons_Add_Sample.md) | This sample demonstrates the creation of a balloon. |
| [Find component referenced by balloon](../../sample-programs/BalloonValueSet_ReferencedRow_Sample.md) | This sample demonstrates how to find the component that a balloon references. |
| [Custom Table - create](../../sample-programs/CustomTables_Sample.md) | This sample demonstrates how to create a custom table. |
| [Title Block Definition Create and Insert](../../sample-programs/TitleBlockDefinition_Sample.md) | This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet. |
| [Copying a title block definition](../../sample-programs/TitleBlockDefinition_CopyTo_Sample.md) | This sample demonstrates copying a title block definition from one drawing to another and replacing the existing title blocks in the drawing with the new title block. |

## Version

Introduced in version 4
