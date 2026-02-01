# ToolPresets Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolPresets.h>

## Description

ToolPresets represents a collection of ToolPreset. It provides access and allows the manipulation like removing and extending the list.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](ToolPresets_add.htm) | Creates and inserts a new Preset at the end of the Preset collection of the owning Tool. The new Preset will have the same values as the owning Tool. |
| [classType](ToolPresets_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](ToolPresets_item.htm) | Get Preset by index. |
| [itemsByName](ToolPresets_itemsByName.htm) | Search presets by name. Returns all presets for which the name matches the given pattern. Compare is case insensitive and characters \* and ? are used for wild-card matching. |
| [remove](ToolPresets_remove.htm) | Remove Preset by index from the owning Tool. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](ToolPresets_count.htm) | The number of Presets of the owning Tool. |
| [isValid](ToolPresets_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ToolPresets_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Tool.presets](Tool_presets.htm)

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