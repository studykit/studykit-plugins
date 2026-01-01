# ToolLibraries.urlByLocation Method

Parent Object: [ToolLibraries](ToolLibraries.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolLibraries.h>

## Description

Get the URL for a given LibraryLocations.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolLibraries\_var" is a variable referencing a [ToolLibraries](ToolLibraries.htm) object.```` ``` returnValue = toolLibraries_var.urlByLocation(location) ``` ```` |

"toolLibraries\_var" is a variable referencing a [ToolLibraries](ToolLibraries.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [URL](URL.htm) | Returns the URL for given location. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| location | [LibraryLocations](LibraryLocations.htm) | The LibraryLocations to be converted into an URL. |

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