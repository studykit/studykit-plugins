# Operations.compatibleStrategies Property

Parent Object: [Operations](Operations.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operations.h>

## Description

Gets a list of the strategies that are compatible with the parent setup. This only returns strategies that are allowed to be added based on the active Setup or CAMFolder.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operations\_var" is a variable referencing an Operations object.  ```` ``` # Get the value of the property. propertyValue = operations_var.compatibleStrategies ``` ```` |

"operations\_var" is a variable referencing an Operations object. ```` ``` #include <Cam/Operations/Operations.h>  // Get the value of the property. std::vector<Ptr<OperationStrategy>> propertyValue = operations_var->compatibleStrategies(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [OperationStrategy](OperationStrategy.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Setups From Hole Recognition API Sample](CreateSetupsFromHoleRecognition_Sample.htm) | This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.  The Fusion Manufacturing Extension is required for Hole Recognition.  The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector. |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |