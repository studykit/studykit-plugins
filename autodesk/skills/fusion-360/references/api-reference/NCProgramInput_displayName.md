# NCProgramInput.displayName Property

Parent Object: [NCProgramInput](NCProgramInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgramInput.h>

## Description

Optionally specify the display name that appears in the browser-tree to override the default.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgramInput\_var" is a variable referencing a NCProgramInput object. |

"nCProgramInput\_var" is a variable referencing a NCProgramInput object. ```` ``` #include <Cam/NCProgram/NCProgramInput.h>  // Get the value of the property. string propertyValue = nCProgramInput_var->displayName();  // Set the value of the property, where value_var is a string. bool returnValue = nCProgramInput_var->displayName(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |
| [Turning Workflow API Sample](Turning_Workflow_API_Sample_Sample.htm) | Turning Workflow API Sample This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |