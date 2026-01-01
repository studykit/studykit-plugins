# ToolPreset Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolPreset.h>

## Description

A Preset defines the material specific properties of a Tool.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ToolPreset_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [id](ToolPreset_id.htm) | Gets and sets the identifier of that Preset. The id can be used to select a Preset for a Operation. |
| [isValid](ToolPreset_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](ToolPreset_name.htm) | Gets and sets the name of that Preset. |
| [objectType](ToolPreset_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parameters](ToolPreset_parameters.htm) | Gets the CAMParameters collection for this Preset. |

## Accessed From

[CAMTemplateOperationInput.toolPreset](CAMTemplateOperationInput_toolPreset.htm), [Operation.toolPreset](Operation_toolPreset.htm), [OperationInput.toolPreset](OperationInput_toolPreset.htm), [ToolPresets.add](ToolPresets_add.htm), [ToolPresets.item](ToolPresets_item.htm), [ToolPresets.itemsByName](ToolPresets_itemsByName.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |