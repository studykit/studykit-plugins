# OperationStrategy.name Property

Parent Object: [OperationStrategy](OperationStrategy.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/OperationStrategy.h>

## Description

Get the name of the strategy. This is equivalent to the Operation's strategy property. Use as strategy parameter when creating a OperationInput.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operationStrategy\_var" is a variable referencing an OperationStrategy object. |

"operationStrategy\_var" is a variable referencing an OperationStrategy object. ```` ``` #include <Cam/Operations/OperationStrategy.h>  // Get the value of the property. string propertyValue = operationStrategy_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

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