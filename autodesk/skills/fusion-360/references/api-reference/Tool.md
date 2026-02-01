# Tool Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Tools/Tool.h>

## Description

Represents a Tool.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Tool_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createFromJson](Tool_createFromJson.htm) | Creates a Tool object from given JSON string. |
| [createFromP21](Tool_createFromP21.htm) | Creates a Tool object given a string containing a tool defined using the P21 format. Throws an error if the given string does not conform to the P21 format. |
| [toJson](Tool_toJson.htm) | Generates and returns a JSON string that contains a description of this tool. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](Tool_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Tool_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parameters](Tool_parameters.htm) | Gets the CAMParameters collection associated with this tool. This defines all of the settings that describe the details of the tool. |
| [presets](Tool_presets.htm) | Gets the ToolPresets collection associated with this tool. |

## Accessed From

[CAMTemplateOperationInput.tool](CAMTemplateOperationInput_tool.htm), [DocumentToolLibrary.item](DocumentToolLibrary_item.htm), [DocumentToolLibrary.toolsBySetupOrFolder](DocumentToolLibrary_toolsBySetupOrFolder.htm), [Operation.tool](Operation_tool.htm), [OperationInput.tool](OperationInput_tool.htm), [Tool.createFromJson](Tool_createFromJson.htm), [Tool.createFromP21](Tool_createFromP21.htm), [ToolLibrary.item](ToolLibrary_item.htm), [ToolQueryResult.tool](ToolQueryResult_tool.htm)

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