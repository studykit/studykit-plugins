# GraphNode.deleteMe Method![](../images/TestTubeLarge.png)

Parent Object: [GraphNode](GraphNode.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/GraphNode.h>

## Description

Deletes the graphNode and all of its connections.

## Syntax

* [Python](#Python)
* [C++](#C++)

"graphNode\_var" is a variable referencing a [GraphNode](GraphNode.htm) object.```` ``` returnValue = graphNode_var.deleteMe() ``` ```` |

"graphNode\_var" is a variable referencing a [GraphNode](GraphNode.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true in the case where the deletion was successful. All properties and proery objects of this node will become invalid after this call. Output nodes cannot be deleted. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |