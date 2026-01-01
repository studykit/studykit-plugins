# URL Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/URL.h>

## Description

A URL object provides useful and easy-to-use methods for creating, modifying, and analyzing URLs.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](URL_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](URL_create.htm) | Create a new URL by given string. |
| [join](URL_join.htm) | Join this URL with the given path and return the resulting URL. The operation does not alter the current URL. Join inserts a slash '/' to properly extend the path, so that "http://foo".join("bar") will return "http://foo/bar", not "http://foobar". |
| [toString](URL_toString.htm) | Get the entire URL as string. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isURLValid](URL_isURLValid.htm) | Check whether the URL is valid. Ensures that the URL is formatted with a protocol followed by a path which can be empty. The check is independent of the existence of the resource the URL may point to. |
| [isValid](URL_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [leafName](URL_leafName.htm) | Get the leaf name of the URL, which is the section behind the last '/'. |
| [objectType](URL_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parent](URL_parent.htm) | Get the parent URL, represented by the section before the last '/'. |
| [pathName](URL_pathName.htm) | Get the path name of the URL, including the last '/' of the protocol followed by the path of the URL. |
| [protocol](URL_protocol.htm) | Get the protocol scheme of the URL, including the final ':'. |

## Accessed From

[CAMLibrary.childAssetURLs](CAMLibrary_childAssetURLs.htm), [CAMLibrary.childFolderURLs](CAMLibrary_childFolderURLs.htm), [CAMLibrary.createFolder](CAMLibrary_createFolder.htm), [CAMLibrary.urlByLocation](CAMLibrary_urlByLocation.htm), [CAMTemplateLibrary.childAssetURLs](CAMTemplateLibrary_childAssetURLs.htm), [CAMTemplateLibrary.childFolderURLs](CAMTemplateLibrary_childFolderURLs.htm), [CAMTemplateLibrary.createFolder](CAMTemplateLibrary_createFolder.htm), [CAMTemplateLibrary.importTemplate](CAMTemplateLibrary_importTemplate.htm), [CAMTemplateLibrary.updateTemplate](CAMTemplateLibrary_updateTemplate.htm), [CAMTemplateLibrary.urlByLocation](CAMTemplateLibrary_urlByLocation.htm), [Machine.postURL](Machine_postURL.htm), [MachineFromLibraryInput.url](MachineFromLibraryInput_url.htm), [MachineLibrary.childAssetURLs](MachineLibrary_childAssetURLs.htm), [MachineLibrary.childFolderURLs](MachineLibrary_childFolderURLs.htm), [MachineLibrary.createFolder](MachineLibrary_createFolder.htm), [MachineLibrary.importMachine](MachineLibrary_importMachine.htm), [MachineLibrary.urlByLocation](MachineLibrary_urlByLocation.htm), [MachineQuery.url](MachineQuery_url.htm), [PostConfigurationQuery.url](PostConfigurationQuery_url.htm), [PostLibrary.childAssetURLs](PostLibrary_childAssetURLs.htm), [PostLibrary.childFolderURLs](PostLibrary_childFolderURLs.htm), [PostLibrary.createFolder](PostLibrary_createFolder.htm), [PostLibrary.importPostConfiguration](PostLibrary_importPostConfiguration.htm), [PostLibrary.urlByLocation](PostLibrary_urlByLocation.htm), [PostProcessingMachineElement.postURL](PostProcessingMachineElement_postURL.htm), [PrintSettingLibrary.childAssetURLs](PrintSettingLibrary_childAssetURLs.htm), [PrintSettingLibrary.childFolderURLs](PrintSettingLibrary_childFolderURLs.htm), [PrintSettingLibrary.createFolder](PrintSettingLibrary_createFolder.htm), [PrintSettingLibrary.importPrintSetting](PrintSettingLibrary_importPrintSetting.htm), [PrintSettingLibrary.urlByLocation](PrintSettingLibrary_urlByLocation.htm), [PrintSettingQuery.url](PrintSettingQuery_url.htm), [StockMaterialLibrary.childAssetURLs](StockMaterialLibrary_childAssetURLs.htm), [StockMaterialLibrary.childFolderURLs](StockMaterialLibrary_childFolderURLs.htm), [StockMaterialLibrary.createFolder](StockMaterialLibrary_createFolder.htm), [StockMaterialLibrary.importStockMaterial](StockMaterialLibrary_importStockMaterial.htm), [StockMaterialLibrary.urlByLocation](StockMaterialLibrary_urlByLocation.htm), [ToolLibraries.childAssetURLs](ToolLibraries_childAssetURLs.htm), [ToolLibraries.childFolderURLs](ToolLibraries_childFolderURLs.htm), [ToolLibraries.createFolder](ToolLibraries_createFolder.htm), [ToolLibraries.importToolLibrary](ToolLibraries_importToolLibrary.htm), [ToolLibraries.urlByLocation](ToolLibraries_urlByLocation.htm), [ToolQuery.url](ToolQuery_url.htm), [ToolQueryResult.toolLibraryURL](ToolQueryResult_toolLibraryURL.htm), [URL.create](URL_create.htm), [URL.join](URL_join.htm), [URL.parent](URL_parent.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Hole and Pocket Recognition API Sample](HoleAndPocketRecognition_Sample.htm) | This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.  The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.  RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.  The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.  This script works only if the Manufacturing Extension is active. |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |
| [Turning Workflow API Sample](Turning_Workflow_API_Sample_Sample.htm) | Turning Workflow API Sample This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |