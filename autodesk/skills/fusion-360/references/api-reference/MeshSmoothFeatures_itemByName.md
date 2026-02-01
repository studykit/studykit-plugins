# MeshSmoothFeatures.itemByName Method![](../images/TestTubeLarge.png)

Parent Object: [MeshSmoothFeatures](MeshSmoothFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshSmoothFeatures.h>

## Description

Function that returns the specified MeshSmooth feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshSmoothFeatures\_var" is a variable referencing a [MeshSmoothFeatures](MeshSmoothFeatures.htm) object.```` ``` returnValue = meshSmoothFeatures_var.itemByName(name) ``` ```` |

"meshSmoothFeatures\_var" is a variable referencing a [MeshSmoothFeatures](MeshSmoothFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeshSmoothFeature](MeshSmoothFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |