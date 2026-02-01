# MeshCombineFaceGroupsFeature.dissolve Method![](../images/TestTubeLarge.png)

Parent Object: [MeshCombineFaceGroupsFeature](MeshCombineFaceGroupsFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshCombineFaceGroupsFeature.h>

## Description

Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshCombineFaceGroupsFeature\_var" is a variable referencing a [MeshCombineFaceGroupsFeature](MeshCombineFaceGroupsFeature.htm) object.```` ``` returnValue = meshCombineFaceGroupsFeature_var.dissolve() ``` ```` |

"meshCombineFaceGroupsFeature\_var" is a variable referencing a [MeshCombineFaceGroupsFeature](MeshCombineFaceGroupsFeature.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns a bool indicating if the dissolve was successful or not. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |