# ToolQueryResult Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolQueryResult.h>

## Description

The ToolQueryResult represents one result item of a ToolQuery.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ToolQueryResult_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ToolQueryResult_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ToolQueryResult_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [tool](ToolQueryResult_tool.htm) | The Tool that matches the query. |
| [toolItemIndex](ToolQueryResult_toolItemIndex.htm) | The index specifies the index of the Tool inside the ToolLibrary. |
| [toolLibrary](ToolQueryResult_toolLibrary.htm) | The ToolLibrary contains a Tool that matches the query. |
| [toolLibraryURL](ToolQueryResult_toolLibraryURL.htm) | The URL defines the location of the ToolLibrary asset in ToolLibraries. |

## Accessed From

[ToolQuery.execute](ToolQuery_execute.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Hole and Pocket Recognition API Sample](HoleAndPocketRecognition_Sample.htm) | This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.  The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.  RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.  The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.  This script works only if the Manufacturing Extension is active. |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |