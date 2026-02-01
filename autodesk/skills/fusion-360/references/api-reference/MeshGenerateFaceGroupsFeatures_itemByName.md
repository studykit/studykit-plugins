# MeshGenerateFaceGroupsFeatures.itemByName Method![](../images/TestTubeLarge.png)

Parent Object: [MeshGenerateFaceGroupsFeatures](MeshGenerateFaceGroupsFeatures.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshGenerateFaceGroupsFeatures.h>

## Description

Function that returns the specified MeshGenerateFaceGroups feature using the name of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshGenerateFaceGroupsFeatures\_var" is a variable referencing a [MeshGenerateFaceGroupsFeatures](MeshGenerateFaceGroupsFeatures.htm) object.```` ``` returnValue = meshGenerateFaceGroupsFeatures_var.itemByName(name) ``` ```` |

"meshGenerateFaceGroupsFeatures\_var" is a variable referencing a [MeshGenerateFaceGroupsFeatures](MeshGenerateFaceGroupsFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MeshGenerateFaceGroupsFeature](MeshGenerateFaceGroupsFeature.htm) | Returns the specified item or null if the specified name was not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the feature within the collection to return. This is the name seen in the timeline. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |