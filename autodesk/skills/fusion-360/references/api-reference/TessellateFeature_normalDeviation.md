# TessellateFeature.normalDeviation Property![](../images/TestTubeLarge.png)

Parent Object: [TessellateFeature](TessellateFeature.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/TessellateFeature.h>

## Description

Specify maximum angle between the normal vectors of each face on the mesh body. Only valid if tessellateRefinementType is CustomTessellateRefinementType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tessellateFeature\_var" is a variable referencing a TessellateFeature object. |

"tessellateFeature\_var" is a variable referencing a TessellateFeature object. ```` ``` #include <Fusion/MeshBody/TessellateFeature.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = tessellateFeature_var->normalDeviation(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |