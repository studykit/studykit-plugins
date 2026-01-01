# CAMTemplateLibrary Object

Derived from: [CAMLibrary](CAMLibrary.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAMTemplate/CAMTemplateLibrary.h>

## Description

The CAMTemplateLibrary provides access to templates. Using this object you can import templates and get existing templates using a URL.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [childAssetURLs](CAMTemplateLibrary_childAssetURLs.htm) | Get all assets under given URL. |
| [childFolderURLs](CAMTemplateLibrary_childFolderURLs.htm) | Get all library folders under given URL. |
| [childTemplates](CAMTemplateLibrary_childTemplates.htm) | Get all templates by the given parent folder URL. Returns null if there is no folder at the URL. |
| [classType](CAMTemplateLibrary_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createFolder](CAMTemplateLibrary_createFolder.htm) | Create a new folder in the library. Create the folder under given parent URL with given folder name. Add counting suffix, in case a folder with given name already exists. Throw an error if given URL does not point to a valid folder or the URL is read-only. Also throws an error if given folder name is empty. |
| [deleteAsset](CAMTemplateLibrary_deleteAsset.htm) | Delete asset by URL from the library. Throw an error if given URL does not point to a valid asset or the URL is read-only. |
| [deleteFolder](CAMTemplateLibrary_deleteFolder.htm) | Delete folder by URL from the library. Any content of the folder will also be deleted. Throw an error if given URL does not point to a valid folder or the URL is read-only. |
| [displayName](CAMTemplateLibrary_displayName.htm) | Get the localized display name for a given URL. The URL must point to a folder. |
| [doesPathExist](CAMTemplateLibrary_doesPathExist.htm) | ![Preview](../images/TestTubeSmall.png)Checks if the given URL points to an existing folder or asset in the library. |
| [importTemplate](CAMTemplateLibrary_importTemplate.htm) | Import a given template at a specific location. The template will be stored in the library. Throws an error if the given URL is read-only. |
| [templateAtURL](CAMTemplateLibrary_templateAtURL.htm) | Gets a specific template specified by the given URL. Returns null if the specified template does not exist. |
| [updateTemplate](CAMTemplateLibrary_updateTemplate.htm) | Update a template in the library. The library substitutes the existing template at the URL by given template. Throws an error if the URL does not already point to an existing template. If the name member of the CAMTemplate doesn't match the name portion of the URL then this will include a rename operation and the returned URL will reflect the new name. |
| [urlByLocation](CAMTemplateLibrary_urlByLocation.htm) | Get the URL for a given LibraryLocations. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assetTypeName](CAMTemplateLibrary_assetTypeName.htm) | Get the name of the asset type which can be accessed by the library. |
| [isValid](CAMTemplateLibrary_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CAMTemplateLibrary_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAMLibraryManager.templateLibrary](CAMLibraryManager_templateLibrary.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Additive Manufacturing SLA API Sample](AdditiveSLAManufacturingSample_Sample.htm) | Demonstrates how to automate the creation of an additive SLA manufacturing setup.  To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive setup using that manufacturing model as an input.  The setup will select a SLA 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically oriented and arranged within the build area of the selected SLA machine. This script will also create support structures, based on the orientation of each component.  The support and orientation operations are created from a template. The script further demonstrates how to wrap script code into a command such that only one undo entry is created for the entire script instead of one entry per internal action. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |