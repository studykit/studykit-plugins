# CAMLibraryManager.postLibrary Property

Parent Object: [CAMLibraryManager](CAMLibraryManager.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Global/CAMLibraryManager.h>

## Description

The PostLibrary provides access to postConfigurations.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMLibraryManager\_var" is a variable referencing a CAMLibraryManager object. |

"cAMLibraryManager\_var" is a variable referencing a CAMLibraryManager object. ```` ``` #include <Cam/Global/CAMLibraryManager.h>  // Get the value of the property. Ptr<PostLibrary> propertyValue = cAMLibraryManager_var->postLibrary(); ``` ```` |

## Property Value

This is a read only property whose value is a [PostLibrary](PostLibrary.htm).

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