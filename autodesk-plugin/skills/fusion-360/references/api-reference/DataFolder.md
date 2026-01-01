# DataFolder Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFolder.h>

## Description

A data folder that contains a collection of data items.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DataFolder_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](DataFolder_deleteMe.htm) | Deletes this folder item. |
| [uploadAssembly](DataFolder_uploadAssembly.htm) | Uploads a set of files that represent an assembly There should only be a single top-level assembly file but there can be any number of other files that represent sub-assemblies. |
| [uploadFile](DataFolder_uploadFile.htm) | Uploads a single file to this directory. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [dataFiles](DataFolder_dataFiles.htm) | Returns a collection containing all of the items within this folder, excluding folders. Use the dataFolders property to get the folders. |
| [dataFolders](DataFolder_dataFolders.htm) | Returns a collection containing all of the folders within this folder. |
| [id](DataFolder_id.htm) | Returns the unique ID for this folder. This is the same id used in the APS Data Management API. |
| [isRoot](DataFolder_isRoot.htm) | Indicates if this folder is the root folder within the parent project. |
| [isValid](DataFolder_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](DataFolder_name.htm) | Gets and sets the displayed name of this folder. |
| [objectType](DataFolder_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentFolder](DataFolder_parentFolder.htm) | Returns the parent folder this folder is contained within. Returns null if this is the project's root folder. |
| [parentProject](DataFolder_parentProject.htm) | Returns the parent project that owns this folder. |

## Accessed From

[CloudFileDialog.dataFolder](CloudFileDialog_dataFolder.htm), [CopyDesignFileInput.targetFolder](CopyDesignFileInput_targetFolder.htm), [CopyFileInput.targetFolder](CopyFileInput_targetFolder.htm), [Data.activeFolder](Data_activeFolder.htm), [Data.findFolderById](Data_findFolderById.htm), [DataFile.parentFolder](DataFile_parentFolder.htm), [DataFolder.parentFolder](DataFolder_parentFolder.htm), [DataFolders.add](DataFolders_add.htm), [DataFolders.asArray](DataFolders_asArray.htm), [DataFolders.item](DataFolders_item.htm), [DataFolders.itemById](DataFolders_itemById.htm), [DataFolders.itemByName](DataFolders_itemByName.htm), [DataProject.rootFolder](DataProject_rootFolder.htm), [DesignDataFile.parentFolder](DesignDataFile_parentFolder.htm), [NCProgram.fusionHubFolder](NCProgram_fusionHubFolder.htm)

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |