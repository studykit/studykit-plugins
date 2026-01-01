# Graph.getNode Method![](../images/TestTubeLarge.png)

Parent Object: [Graph](Graph.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/Graph.h>

## Description

Get node with the given name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"graph\_var" is a variable referencing a [Graph](Graph.htm) object.```` ``` returnValue = graph_var.getNode(name) ``` ```` |

"graph\_var" is a variable referencing a [Graph](Graph.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [GraphNode](GraphNode.htm) | The node if found, null otherwise. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | Name to search for. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |