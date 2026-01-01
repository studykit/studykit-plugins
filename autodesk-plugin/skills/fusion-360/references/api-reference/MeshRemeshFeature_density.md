# MeshRemeshFeature.density Property![](../images/TestTubeLarge.png)

Parent Object: [MeshRemeshFeature](MeshRemeshFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshRemeshFeature.h>

## Description

Controls the density of the newly created faces of the re-meshed mesh. The values can range between 0 and 1.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshRemeshFeature\_var" is a variable referencing a MeshRemeshFeature object. |

"meshRemeshFeature\_var" is a variable referencing a MeshRemeshFeature object. ```` ``` #include <Fusion/MeshBody/MeshRemeshFeature.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = meshRemeshFeature_var->density(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |