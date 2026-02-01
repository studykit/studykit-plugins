# MeshGenerateFaceGroupsFeature.angleThreshold Property![](../images/TestTubeLarge.png)

Parent Object: [MeshGenerateFaceGroupsFeature](MeshGenerateFaceGroupsFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshGenerateFaceGroupsFeature.h>

## Description

Controls the angle threshold during the face group generation. The values can range between 0 and pi/2. Only valid if meshGenerateFaceGroupsMethodType is FastGenerateFaceGroupsType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshGenerateFaceGroupsFeature\_var" is a variable referencing a MeshGenerateFaceGroupsFeature object. |

"meshGenerateFaceGroupsFeature\_var" is a variable referencing a MeshGenerateFaceGroupsFeature object. ```` ``` #include <Fusion/MeshBody/MeshGenerateFaceGroupsFeature.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = meshGenerateFaceGroupsFeature_var->angleThreshold(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |