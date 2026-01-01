# NCPrograms.createInput Method

Parent Object: [NCPrograms](NCPrograms.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCPrograms.h>

## Description

Create a new NCProgramInput object. Use properties and methods on this object to define the NC program you want to create and then use the Add method, passing in the NCProgramInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCPrograms\_var" is a variable referencing a [NCPrograms](NCPrograms.htm) object.```` ``` returnValue = nCPrograms_var.createInput() ``` ```` |

"nCPrograms\_var" is a variable referencing a [NCPrograms](NCPrograms.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [NCProgramInput](NCProgramInput.htm) | Returns a new NCProgramInput object. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Basic Milling Workflow Sample](BasicMillingWorkflowSample_Sample.htm) | Demonstrates the creation of a basic milling workflow from script Demonstrates creating a setup, searching tool library to retrieve a tool, create a couple of machining operations and a NC program, ready for post processing.  Use the 2D Strategies model from the Fusion CAM Samples folder as your CAD model. |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |
| [Turning Workflow API Sample](Turning_Workflow_API_Sample_Sample.htm) | Turning Workflow API Sample This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |