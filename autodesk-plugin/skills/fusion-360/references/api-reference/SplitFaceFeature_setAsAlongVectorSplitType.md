# SplitFaceFeature.setAsAlongVectorSplitType Method

Parent Object: [SplitFaceFeature](SplitFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeature.h>

## Description

Sets the split type to project the splitting tool along the direction defined by the specified entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeature\_var" is a variable referencing a [SplitFaceFeature](SplitFaceFeature.htm) object.```` ``` returnValue = splitFaceFeature_var.setAsAlongVectorSplitType(splittingTool, directionEntity) ``` ```` |

"splitFaceFeature\_var" is a variable referencing a [SplitFaceFeature](SplitFaceFeature.htm) object.  ```` ``` #include <Fusion/Features/SplitFaceFeature.h>  returnValue = splitFaceFeature_var->setAsAlongVectorSplitType(splittingTool, directionEntity); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true is setting the split type was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| splittingTool | [Base](Base.htm) | Input entity(s) that defines the splitting tool. The splitting tool can be a single entity or an ObjectCollection containing faces or sketch curves. If faces are input, the edges of the face are used as the splitting tool. |
| directionEntity | [Base](Base.htm) | An entity that defines the direction of projection of the splitting tool. This can be a linear BRepEdge, SketchLine, ConstructionLine, or a planar face where the face normal is used. |

## Version

Introduced in version May 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |