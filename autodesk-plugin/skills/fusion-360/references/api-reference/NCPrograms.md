# NCPrograms Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCPrograms.h>

## Description

Container for all NC programs. Referenced from CAM product to access NC programs in a document, similar to what Setups is for all setup objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](NCPrograms_add.htm) | Creates a new NC program. |
| [classType](NCPrograms_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createInput](NCPrograms_createInput.htm) | Create a new NCProgramInput object. Use properties and methods on this object to define the NC program you want to create and then use the Add method, passing in the NCProgramInput object. |
| [item](NCPrograms_item.htm) | Function that returns the specified NC program using an index into the collection. |
| [itemByName](NCPrograms_itemByName.htm) | Returns the NC program with the specified name. |
| [itemByOperationId](NCPrograms_itemByOperationId.htm) | Returns the NC program with the specified operation id. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](NCPrograms_count.htm) | The number of items in the collection. |
| [isValid](NCPrograms_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](NCPrograms_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CAM.ncPrograms](CAM_ncPrograms.htm)

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