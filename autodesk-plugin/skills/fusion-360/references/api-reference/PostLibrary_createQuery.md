# PostLibrary.createQuery Method

Parent Object: [PostLibrary](PostLibrary.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Post/PostLibrary.h>

## Description

Creates a new PostConfigurationQuery that is used to query the library for post configurations matching the query.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postLibrary\_var" is a variable referencing a [PostLibrary](PostLibrary.htm) object.```` ``` returnValue = postLibrary_var.createQuery(location) ``` ```` |

"postLibrary\_var" is a variable referencing a [PostLibrary](PostLibrary.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PostConfigurationQuery](PostConfigurationQuery.htm) | Returns a new PostConfigurationQuery. The query is predefined by given parameter. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| location | [LibraryLocations](LibraryLocations.htm) | The location specifies the LibraryLocations where to search for in the post library. |

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