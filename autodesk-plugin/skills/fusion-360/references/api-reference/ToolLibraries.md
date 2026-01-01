# ToolLibraries Object

Derived from: [CAMLibrary](CAMLibrary.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolLibraries.h>

## Description

The ToolLibraries object provides utilities to access, import and update tool libraries.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [childAssetURLs](ToolLibraries_childAssetURLs.htm) | Get all assets under given URL. |
| [childFolderURLs](ToolLibraries_childFolderURLs.htm) | Get all library folders under given URL. |
| [classType](ToolLibraries_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createFolder](ToolLibraries_createFolder.htm) | Create a new folder in the library. Create the folder under given parent URL with given folder name. Add counting suffix, in case a folder with given name already exists. Throw an error if given URL does not point to a valid folder or the URL is read-only. Also throws an error if given folder name is empty. |
| [createQuery](ToolLibraries_createQuery.htm) | Creates a new ToolQuery that is used to query the library for tools matching the query. |
| [deleteAsset](ToolLibraries_deleteAsset.htm) | Delete asset by URL from the library. Throw an error if given URL does not point to a valid asset or the URL is read-only. |
| [deleteFolder](ToolLibraries_deleteFolder.htm) | Delete folder by URL from the library. Any content of the folder will also be deleted. Throw an error if given URL does not point to a valid folder or the URL is read-only. |
| [displayName](ToolLibraries_displayName.htm) | Get the localized display name for a given URL. The URL must point to a folder. |
| [doesPathExist](ToolLibraries_doesPathExist.htm) | ![Preview](../images/TestTubeSmall.png)Checks if the given URL points to an existing folder or asset in the library. |
| [importToolLibrary](ToolLibraries_importToolLibrary.htm) | Import a given ToolLibrary from a specific location. The imported ToolLibrary can be accessed through this ToolLibraries object. Throws an error, if the given URL is read-only. |
| [toolLibraryAtURL](ToolLibraries_toolLibraryAtURL.htm) | Get a specific ToolLibrary by given URL. Returns null, if the URL does not exist. |
| [updateToolLibrary](ToolLibraries_updateToolLibrary.htm) | Update ToolLibrary in ToolLibraries. Overrides the URL by given ToolLibrary. Throws an error if the URL does not already point to an existing ToolLibrary. |
| [urlByLocation](ToolLibraries_urlByLocation.htm) | Get the URL for a given LibraryLocations. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assetTypeName](ToolLibraries_assetTypeName.htm) | Get the name of the asset type which can be accessed by the library. |
| [isValid](ToolLibraries_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ToolLibraries_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAMLibraryManager.toolLibraries](CAMLibraryManager_toolLibraries.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Basic Milling Workflow Sample](BasicMillingWorkflowSample_Sample.htm) | Demonstrates the creation of a basic milling workflow from script Demonstrates creating a setup, searching tool library to retrieve a tool, create a couple of machining operations and a NC program, ready for post processing.  Use the 2D Strategies model from the Fusion CAM Samples folder as your CAD model. |
| [Hole and Pocket Recognition API Sample](HoleAndPocketRecognition_Sample.htm) | This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.  The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.  RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.  The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.  This script works only if the Manufacturing Extension is active. |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |
| [Turning Workflow API Sample](Turning_Workflow_API_Sample_Sample.htm) | Turning Workflow API Sample This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |
| [Wood Routing Workflow Sample](WoodRoutingSample_Sample.htm) | This script demonstrates routing wood panels. When running the sample, it assumes you have an open design containing one or more "panels" oriented flat in the X-Y plane. The script creates a setup and a 2D contour operation with tabs to route the panels from a standard sheet. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |