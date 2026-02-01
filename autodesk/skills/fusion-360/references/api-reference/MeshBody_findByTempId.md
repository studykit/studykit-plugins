# MeshBody.findByTempId Method![](../images/TestTubeLarge.png)

Parent Object: [MeshBody](MeshBody.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBody.h>

## Description

Returns the face group with the temporary id.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBody\_var" is a variable referencing a [MeshBody](MeshBody.htm) object.```` ``` returnValue = meshBody_var.findByTempId(tempId) ``` ```` |

"meshBody\_var" is a variable referencing a [MeshBody](MeshBody.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Base](Base.htm) | Returns the face group with the given tempId. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| tempId | integer | The ID of the face group to find. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |