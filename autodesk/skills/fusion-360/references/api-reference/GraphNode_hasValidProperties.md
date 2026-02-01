# GraphNode.hasValidProperties Method![](../images/TestTubeLarge.png)

Parent Object: [GraphNode](GraphNode.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/GraphNode.h>

## Description

Check if the graph node properties are valid.

## Syntax

* [Python](#Python)
* [C++](#C++)

"graphNode\_var" is a variable referencing a [GraphNode](GraphNode.htm) object.```` ``` returnValue = graphNode_var.hasValidProperties() ``` ```` |

"graphNode\_var" is a variable referencing a [GraphNode](GraphNode.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | True if the node has good inputs for its properties, false otherwise. |

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |