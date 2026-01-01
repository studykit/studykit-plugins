# ToolPreset.name Property

Parent Object: [ToolPreset](ToolPreset.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolPreset.h>

## Description

Gets and sets the name of that Preset.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolPreset\_var" is a variable referencing a ToolPreset object. |

"toolPreset\_var" is a variable referencing a ToolPreset object. ```` ``` #include <Cam/Tools/ToolPreset.h>  // Get the value of the property. string propertyValue = toolPreset_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = toolPreset_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

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