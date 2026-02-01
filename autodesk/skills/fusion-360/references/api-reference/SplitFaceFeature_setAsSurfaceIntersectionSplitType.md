# SplitFaceFeature.setAsSurfaceIntersectionSplitType Method

Parent Object: [SplitFaceFeature](SplitFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeature.h>

## Description

Set the split type to be a surface to surface intersection. If the split tool is a curve it will be extruded into a surface to use in the split. If it's a surface, the surface will be used and optionally extended to fully intersect the faces to be split.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeature\_var" is a variable referencing a [SplitFaceFeature](SplitFaceFeature.htm) object.```` ``` returnValue = splitFaceFeature_var.setAsSurfaceIntersectionSplitType(splittingTool, isSplittingToolExtended) ``` ```` |

"splitFaceFeature\_var" is a variable referencing a [SplitFaceFeature](SplitFaceFeature.htm) object.  ```` ``` #include <Fusion/Features/SplitFaceFeature.h>  returnValue = splitFaceFeature_var->setAsSurfaceIntersectionSplitType(splittingTool, isSplittingToolExtended); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true is setting the split type was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| splittingTool | [Base](Base.htm) | Input entity(s) that defines the splitting tool. The splitting tool can be a single entity or an ObjectCollection containing solid and/or open bodies, construction planes, faces, or sketch curves that partially or fully intersect the faces that are being split. |
| isSplittingToolExtended | Boolean | Specifies if the splitting tool should be extended so that is fully intersects the faces to be split. |

## Version

Introduced in version May 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |