# SplitFaceFeature.setAsClosestPointSplitType Method

Parent Object: [SplitFaceFeature](SplitFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeature.h>

## Description

Sets the split type to be a curve that defined by projecting the splitting curve to the closest point on the surface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeature\_var" is a variable referencing a [SplitFaceFeature](SplitFaceFeature.htm) object.```` ``` returnValue = splitFaceFeature_var.setAsClosestPointSplitType(splittingTool) ``` ```` |

"splitFaceFeature\_var" is a variable referencing a [SplitFaceFeature](SplitFaceFeature.htm) object.  ```` ``` #include <Fusion/Features/SplitFaceFeature.h>  returnValue = splitFaceFeature_var->setAsClosestPointSplitType(splittingTool); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if setting the closest point split type was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| splittingTool | [Base](Base.htm) | Input entity(s) that defines the splitting tool. The splitting tool can be a single entity or an ObjectCollection containing faces or sketch curves. If faces are input, the edges of the face are used as the splitting tool. |

## Version

Introduced in version May 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |