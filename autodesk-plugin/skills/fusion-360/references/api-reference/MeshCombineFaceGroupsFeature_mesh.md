# MeshCombineFaceGroupsFeature.mesh Property![](../images/TestTubeLarge.png)

Parent Object: [MeshCombineFaceGroupsFeature](MeshCombineFaceGroupsFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshCombineFaceGroupsFeature.h>

## Description

Gets the input mesh body. The actual mesh body is set implicitly by the input face groups.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshCombineFaceGroupsFeature\_var" is a variable referencing a MeshCombineFaceGroupsFeature object. |

"meshCombineFaceGroupsFeature\_var" is a variable referencing a MeshCombineFaceGroupsFeature object. ```` ``` #include <Fusion/MeshBody/MeshCombineFaceGroupsFeature.h>  // Get the value of the property. Ptr<Base> propertyValue = meshCombineFaceGroupsFeature_var->mesh(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |