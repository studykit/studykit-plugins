# NCProgramInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgramInput.h>

## Description

The NCProgramInput holds all necessary information to create a new NC program. It is needed for the NCPrograms.add method to instantiate a new NC program.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](NCProgramInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [displayName](NCProgramInput_displayName.htm) | Optionally specify the display name that appears in the browser-tree to override the default. |
| [isValid](NCProgramInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](NCProgramInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [operations](NCProgramInput_operations.htm) | Gets and sets the operations which will be included in the NC program. Valid input contains any number of operations, setups or folders. For setups and folders all child operations will be added. Operations will be post processed in setup order, with operations from the same setup grouped together. Setting the nc\_program\_orderByTool BooleanParameterValue on the parameters property to true will reorder operations across multiple setups to reduce the number of tool changes. When the list of operations is associated to one setup and the setup has defined its job\_programName or job\_programComment parameters, then those values are applied to the nc\_program\_name and nc\_program\_comment parameters accordingly. |
| [parameters](NCProgramInput_parameters.htm) | Get all parameters for the current NC program. Parameters are initialized by user defaults. Configure operation parameters before creation for a better performance. |

## Accessed From

[NCPrograms.createInput](NCPrograms_createInput.htm)

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