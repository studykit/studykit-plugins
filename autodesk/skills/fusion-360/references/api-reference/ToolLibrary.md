# ToolLibrary Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolLibrary.h>

## Description

ToolLibrary represents a collection of Tool objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ToolLibrary_add.htm) | Inserts a Tool at the end of the ToolLibrary. |
| [classType](ToolLibrary_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createEmpty](ToolLibrary_createEmpty.htm) | Creates an empty ToolLibrary. |
| [createFromJson](ToolLibrary_createFromJson.htm) | Creates a ToolLibrary by given JSON-string. Raises an error if the given JSON is invalid. |
| [createQuery](ToolLibrary_createQuery.htm) | Creates a new ToolQuery that is used to query the library for tools matching the query. |
| [item](ToolLibrary_item.htm) | Get Tool by index in ToolLibrary. |
| [remove](ToolLibrary_remove.htm) | Remove Tool by index from ToolLibrary. |
| [toJson](ToolLibrary_toJson.htm) | Generate and return JSON string that contains all tools of that list. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ToolLibrary_count.htm) | The number of tools in the ToolLibrary. |
| [isValid](ToolLibrary_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ToolLibrary_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[DocumentToolLibrary.createEmpty](DocumentToolLibrary_createEmpty.htm), [DocumentToolLibrary.createFromJson](DocumentToolLibrary_createFromJson.htm), [ToolLibraries.toolLibraryAtURL](ToolLibraries_toolLibraryAtURL.htm), [ToolLibrary.createEmpty](ToolLibrary_createEmpty.htm), [ToolLibrary.createFromJson](ToolLibrary_createFromJson.htm), [ToolQueryResult.toolLibrary](ToolQueryResult_toolLibrary.htm)

## Derived Classes

[DocumentToolLibrary](DocumentToolLibrary.htm)

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