# CAM.temporaryFolder Property

Parent Object: [CAM](CAM.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

Gets the folder for temporary files.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM\_var" is a variable referencing a CAM object. |

"cAM\_var" is a variable referencing a CAM object. ```` ``` #include <Cam/CAM/CAM.h>  // Get the value of the property. string propertyValue = cAM_var->temporaryFolder(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Post Toolpaths API Sample](PostToolpaths_Sample_Sample.htm) | Demonstrates posting toolpaths in the active document. |
| [Turning Workflow API Sample](Turning_Workflow_API_Sample_Sample.htm) | Turning Workflow API Sample This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |