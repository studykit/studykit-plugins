# MeshBody.moveToComponent Method![](../images/TestTubeLarge.png)

Parent Object: [MeshBody](MeshBody.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBody.h>

## Description

Moves this mesh body from it's current component into the root component or the component owned by the specified occurrence.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBody\_var" is a variable referencing a [MeshBody](MeshBody.htm) object.```` ``` returnValue = meshBody_var.moveToComponent(target) ``` ```` |

"meshBody\_var" is a variable referencing a [MeshBody](MeshBody.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeshBody](MeshBody.htm) | Returns the moved mesh body or null in the case the move failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| target | [Base](Base.htm) | The target can be either the root component or an occurrence.   In the case where an occurrence is specified, the mesh body will be moved into the parent component of the target occurrence and the target occurrence defines the transform of how the mesh body will be copied so that the body maintains it's same position with respect to the assembly. |

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |