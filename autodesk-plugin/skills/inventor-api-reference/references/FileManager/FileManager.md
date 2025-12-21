# FileManager Object

## Description

The FileManager object provides access to file-related utility functions.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CanCADFileBeAssociativelyImported](../FileManager/FileManager_CanCADFileBeAssociativelyImported.md) | Method that checks whether a foreign CAD file can be associatively imported into Inventor document or not. |
| [CopyFile](../FileManager/FileManager_CopyFile.md) | Method that copies the specified Autodesk Inventor file (.ipt, .idw, .ipt etc.) from one location to another. |
| [DeleteFile](../FileManager/FileManager_DeleteFile.md) | Method that deletes the specified file. |
| [GetAutoCADBlockDefinitions](../FileManager/FileManager_GetAutoCADBlockDefinitions.md) | Method that returns the names of all the AutoCAD block definitions contained within the input DWG file. The input file can be an AutoCAD DWG or an Inventor DWG. |
| [GetDesignViewRepresentations](../FileManager/FileManager_GetDesignViewRepresentations.md) | Method that returns the names of all the design view representations contained within the input file (either \*.iam, \*.ipt or \*.idv). |
| [GetDWGDocumentReferences](../FileManager/FileManager_GetDWGDocumentReferences.md) | Gets the set of direct file references from a DWG file. |
| [GetEmbeddedDocumentShortName](../FileManager/FileManager_GetEmbeddedDocumentShortName.md) | Method that returns the short filename of an embedded document path. |
| [GetExpressGraphicsStatus](../FileManager/FileManager_GetExpressGraphicsStatus.md) | Returns a value indicating the current state of the express graphics in the specified assembly. |
| [GetFileNameFromIdentifier](../FileManager/FileManager_GetFileNameFromIdentifier.md) | Property that returns the fully qualified name of a file using its unique identifier. The identifier must have been obtained from the GetIdentifierFromFileName method. |
| [GetFullDocumentName](../FileManager/FileManager_GetFullDocumentName.md) | Returns the full document name which is a unique identifier for an open Document. The returned string is the full file name concatenated with the model state name for a part or assembly document. |
| [GetFullFileName](../FileManager/FileManager_GetFullFileName.md) | Returns the full file name given its full document name. |
| [GetIdentifierFromFileName](../FileManager/FileManager_GetIdentifierFromFileName.md) | Creates and returns a unique, persistent identifier for the specified file. |
| [GetLastActiveDesignViewRepresentation](../FileManager/FileManager_GetLastActiveDesignViewRepresentation.md) | Method that returns the name of the design view representation that was active when the file was last saved. |
| [GetLastActiveModelState](../FileManager/FileManager_GetLastActiveModelState.md) | Method that returns the name of the model state that was active when the file was last saved. |
| [GetModelStateName](../FileManager/FileManager_GetModelStateName.md) | Method that returns the name of the model state given its full document name. |
| [GetModelStates](../FileManager/FileManager_GetModelStates.md) | Method that returns the names of all the model states contained within the input file. |
| [GetPositionalRepresentations](../FileManager/FileManager_GetPositionalRepresentations.md) | Method that returns the names of all the positional representations contained within the input assembly file. |
| [GetRevitEngineInstallationStatus](../FileManager/FileManager_GetRevitEngineInstallationStatus.md) | Method that returns the Revit engine installation status for available versions. |
| [GetRevitFileVersionCreated](../FileManager/FileManager_GetRevitFileVersionCreated.md) | Method that returns the Revit version that the Revit file was created with. |
| [GetSHXFontList](../FileManager/FileManager_GetSHXFontList.md) | Method that gets the array of strings containing the SHX font name list. |
| [GetTemplateFile](../FileManager/FileManager_GetTemplateFile.md) | Method that specifies the template to use when creating a file. |
| [GetTemplateFileWithOptions](../FileManager/FileManager_GetTemplateFileWithOptions.md) | Method that gets a template file that can be used to create a new document. |
| [InstallRevitEngineVersion](../FileManager/FileManager_InstallRevitEngineVersion.md) | Method that tries to install specified Revit engine and returns the installation status. The installation is asynchronous, and this returns kInstallationInProcessStatus if the installation is started. |
| [IsEmbeddedDocumentPath](../FileManager/FileManager_IsEmbeddedDocumentPath.md) | Method that returns whether the input string indicates an embedded document path. |
| [IsFileNameValid](../FileManager/FileManager_IsFileNameValid.md) | Validate the input filename and replace illegal filename characters with something more appropriate. |
| [IsFutureCADFile](../FileManager/FileManager_IsFutureCADFile.md) | Method that returns whether the input CAD file is a future CAD file. If an invalid CAD filename is provided an error would occur. |
| [IsInventorComponent](../FileManager/FileManager_IsInventorComponent.md) | Returns whether the input file is an Inventor Component (part or assembly). |
| [IsInventorDWG](../FileManager/FileManager_IsInventorDWG.md) | Method that returns whether the input file is an Inventor DWG file. |
| [MoveFile](../FileManager/FileManager_MoveFile.md) | Method that moves the specified file from one location to another. |
| [ReferencedDocumentCount](../FileManager/FileManager_ReferencedDocumentCount.md) | Returns the number of uniquely referenced documents the input document had at the time it was last saved. This is the number that is used in determining whether or not an assembly will open in Express mode or Full mode. |
| [RefreshAllDocuments](../FileManager/FileManager_RefreshAllDocuments.md) | Refreshes all documents in memory to the latest version on disk. |
| [SoftwareVersionSaved](../FileManager/FileManager_SoftwareVersionSaved.md) | Returns the object that encapsulates the version of the software with which this file was last saved. |
| [WillOpenExpressDefault](../FileManager/FileManager_WillOpenExpressDefault.md) | Returns whether the input assembly will open in Express mode by default. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FileManager/FileManager_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [FileManagerEvents](../FileManager/FileManager_FileManagerEvents.md) | Property that gets the object that fires the File Manager related events. |
| [Files](../FileManager/FileManager_Files.md) | Property that returns the FilesEnumerator object |
| [FileSystemObject](../FileManager/FileManager_FileSystemObject.md) | Gets the Scripting.FileSystemObject in Inventor process. |
| [Type](../FileManager/FileManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Application.FileManager](../Application/Application_FileManager.md), [ApprenticeServer.FileManager](../ApprenticeServer/ApprenticeServer_FileManager.md), [ApprenticeServerComponent.FileManager](../ApprenticeServerComponent/ApprenticeServerComponent_FileManager.md), [InventorServer.FileManager](InventorServer_FileManager.md), [InventorServerObject.FileManager](InventorServerObject_FileManager.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |
| [Open assembly using last model state](../../sample-programs/GetLastActiveModelState_Sample.md) | This sample demonstrates how to open an assembly document in its last active model state. |
| [Create sheet metal lofted flange feature](../../sample-programs/LoftedFlangeFeatures_Add_Sample.md) | The following sample demonstrates the creation of a sheet metal lofted flange feature. |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |
| [Sketch profile control](../../sample-programs/ProfilePath_AddsMaterial_Sample.md) | This sample demonstrates the usage of the Profiles API to control the shape of the profile. The sample creates three concntric circles and creates an extrusion of the region between the inner circles. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Sheet Metal Feature Display](../../sample-programs/SheetMetalComponentDefinition_Sample.md) | This sample illustrates getting basic information from the various sheet metal features. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |

## Version

Introduced in version 6
