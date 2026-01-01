# ToolPreset.parameters Property

Parent Object: [ToolPreset](ToolPreset.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolPreset.h>

## Description

Gets the CAMParameters collection for this Preset.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolPreset\_var" is a variable referencing a ToolPreset object. |

"toolPreset\_var" is a variable referencing a ToolPreset object. ```` ``` #include <Cam/Tools/ToolPreset.h>  // Get the value of the property. Ptr<CAMParameters> propertyValue = toolPreset_var->parameters(); ``` ```` |

## Property Value

This is a read only property whose value is a [CAMParameters](CAMParameters.htm).

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