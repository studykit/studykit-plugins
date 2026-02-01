# ToolLibraries.childAssetURLs Method

Parent Object: [ToolLibraries](ToolLibraries.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Tools/ToolLibraries.h>

## Description

Get all assets under given URL.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolLibraries\_var" is a variable referencing a [ToolLibraries](ToolLibraries.htm) object.```` ``` returnValue = toolLibraries_var.childAssetURLs(url) ``` ```` |

"toolLibraries\_var" is a variable referencing a [ToolLibraries](ToolLibraries.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [URL](URL.htm)[] | Returns list of asset URLs at given location. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | [URL](URL.htm) | The URL to the parent folder. |

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