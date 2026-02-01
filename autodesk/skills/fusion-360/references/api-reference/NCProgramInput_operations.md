# NCProgramInput.operations Property

Parent Object: [NCProgramInput](NCProgramInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgramInput.h>

## Description

Gets and sets the operations which will be included in the NC program. Valid input contains any number of operations, setups or folders. For setups and folders all child operations will be added. Operations will be post processed in setup order, with operations from the same setup grouped together. Setting the nc\_program\_orderByTool BooleanParameterValue on the parameters property to true will reorder operations across multiple setups to reduce the number of tool changes. When the list of operations is associated to one setup and the setup has defined its job\_programName or job\_programComment parameters, then those values are applied to the nc\_program\_name and nc\_program\_comment parameters accordingly.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgramInput\_var" is a variable referencing a NCProgramInput object. |

"nCProgramInput\_var" is a variable referencing a NCProgramInput object. ```` ``` #include <Cam/NCProgram/NCProgramInput.h>  // Get the value of the property. std::vector<Ptr<OperationBase>> propertyValue = nCProgramInput_var->operations();  // Set the value of the property, where value_var is an OperationBase. bool returnValue = nCProgramInput_var->operations(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [OperationBase](OperationBase.htm).

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