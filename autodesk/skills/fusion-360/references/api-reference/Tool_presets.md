# Tool.presets Property

Parent Object: [Tool](Tool.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/Tool.h>

## Description

Gets the ToolPresets collection associated with this tool.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tool\_var" is a variable referencing a Tool object. |

"tool\_var" is a variable referencing a Tool object. ```` ``` #include <Cam/Tools/Tool.h>  // Get the value of the property. Ptr<ToolPresets> propertyValue = tool_var->presets(); ``` ```` |

## Property Value

This is a read only property whose value is a [ToolPresets](ToolPresets.htm).

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