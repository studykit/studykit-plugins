# CAMParameters Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CAMParameters.h>

## Description

Collection that provides access to the parameters of an existing operation.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CAMParameters_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](CAMParameters_item.htm) | Function that returns the specified parameter using an index into the collection. |
| [itemByName](CAMParameters_itemByName.htm) | Returns the parameter of the specified id (internal name). |
| [resetToSystemDefaults](CAMParameters_resetToSystemDefaults.htm) | ![Preview](../images/TestTubeSmall.png)Resets each parameter to its system default. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](CAMParameters_count.htm) | The number of items in the collection. |
| [isValid](CAMParameters_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CAMParameters_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAMAdditiveContainer.parameters](CAMAdditiveContainer_parameters.htm), [CAMFolder.parameters](CAMFolder_parameters.htm), [CAMHoleRecognition.parameters](CAMHoleRecognition_parameters.htm), [CAMPattern.parameters](CAMPattern_parameters.htm), [CAMTemplateOperationInput.parameters](CAMTemplateOperationInput_parameters.htm), [NCProgram.parameters](NCProgram_parameters.htm), [NCProgram.postParameters](NCProgram_postParameters.htm), [NCProgramInput.parameters](NCProgramInput_parameters.htm), [Operation.parameters](Operation_parameters.htm), [OperationBase.parameters](OperationBase_parameters.htm), [OperationInput.parameters](OperationInput_parameters.htm), [PostProcessingMachineElement.postParameters](PostProcessingMachineElement_postParameters.htm), [PrintSetting.parameters](PrintSetting_parameters.htm), [PrintSettingItem.parameters](PrintSettingItem_parameters.htm), [Setup.parameters](Setup_parameters.htm), [SetupInput.parameters](SetupInput_parameters.htm), [Tool.parameters](Tool_parameters.htm), [ToolPreset.parameters](ToolPreset_parameters.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [CAM Parameter Modification API Sample](CAMParameterChange_Sample_Sample.htm) | Demonstrates changing parameters of existing toolpaths. |
| [Create Setups From Hole Recognition API Sample](CreateSetupsFromHoleRecognition_Sample.htm) | This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.  The Fusion Manufacturing Extension is required for Hole Recognition.  The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector. |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |
| [Turning Workflow API Sample](Turning_Workflow_API_Sample_Sample.htm) | Turning Workflow API Sample This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |