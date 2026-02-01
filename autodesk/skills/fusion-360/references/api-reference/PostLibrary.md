# PostLibrary Object

Derived from: [CAMLibrary](CAMLibrary.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostLibrary.h>

## Description

The PostLibrary provides access to post configurations. Using this object you can import post configurations and get existing post configurations using either a URL or query to find specific post configurations.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [childAssetURLs](PostLibrary_childAssetURLs.htm) | Get all assets under given URL. |
| [childFolderURLs](PostLibrary_childFolderURLs.htm) | Get all library folders under given URL. |
| [childPostConfigurations](PostLibrary_childPostConfigurations.htm) | Get all posts by the given parent folder URL. Returns null, if the URL does not exist. |
| [classType](PostLibrary_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createFolder](PostLibrary_createFolder.htm) | Create a new folder in the library. Create the folder under given parent URL with given folder name. Add counting suffix, in case a folder with given name already exists. Throw an error if given URL does not point to a valid folder or the URL is read-only. Also throws an error if given folder name is empty. |
| [createQuery](PostLibrary_createQuery.htm) | Creates a new PostConfigurationQuery that is used to query the library for post configurations matching the query. |
| [deleteAsset](PostLibrary_deleteAsset.htm) | Delete asset by URL from the library. Throw an error if given URL does not point to a valid asset or the URL is read-only. |
| [deleteFolder](PostLibrary_deleteFolder.htm) | Delete folder by URL from the library. Any content of the folder will also be deleted. Throw an error if given URL does not point to a valid folder or the URL is read-only. |
| [displayName](PostLibrary_displayName.htm) | Get the localized display name for a given URL. The URL must point to a folder. |
| [doesPathExist](PostLibrary_doesPathExist.htm) | ![Preview](../images/TestTubeSmall.png)Checks if the given URL points to an existing folder or asset in the library. |
| [importPostConfiguration](PostLibrary_importPostConfiguration.htm) | Import a given post configuration at a specific location. The post configuration will be stored in the library. Throws an error, if the given URL is read-only. |
| [postConfigurationAtURL](PostLibrary_postConfigurationAtURL.htm) | Get a specific post configuration by the given URL. Returns null, if the URL does not exist. |
| [urlByLocation](PostLibrary_urlByLocation.htm) | Get the URL for a given LibraryLocations. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assetTypeName](PostLibrary_assetTypeName.htm) | Get the name of the asset type which can be accessed by the library. |
| [isValid](PostLibrary_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](PostLibrary_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAMLibraryManager.postLibrary](CAMLibraryManager_postLibrary.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |
| [Turning Workflow API Sample](Turning_Workflow_API_Sample_Sample.htm) | Turning Workflow API Sample This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |