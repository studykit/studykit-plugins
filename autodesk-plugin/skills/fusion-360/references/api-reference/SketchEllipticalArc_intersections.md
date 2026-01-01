# SketchEllipticalArc.intersections Method

Parent Object: [SketchEllipticalArc](SketchEllipticalArc.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipticalArc.h>

## Description

Get the curves that intersect this curve along with the intersection points (Point3D)

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipticalArc\_var" is a variable referencing a [SketchEllipticalArc](SketchEllipticalArc.htm) object. |

```` ```  #include <Fusion/Sketch/SketchEllipticalArc.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if intersections are found |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sketchCurves | [ObjectCollection](ObjectCollection.htm) | A collection of curves to attempt to find intersections with. Set the value of this parameter to null to use all curves in the sketch for the calculation. |
| intersectingCurves | [ObjectCollection](ObjectCollection.htm) | A collection of the actual intersecting curves |
| intersectionPoints | [ObjectCollection](ObjectCollection.htm) | A collection of intersection points (Point3D) Item numbers in this collection correspond to the item numbers in the intersectingCurves collection. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |