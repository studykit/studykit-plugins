# SketchArc.breakCurve Method

Parent Object: [SketchArc](SketchArc.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchArc.h>

## Description

Breaks a curve into two or three pieces by finding intersections of this curve with all other curves in the sketch and splitting this curve at the nearest intersections to a specified point on the curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchArc\_var" is a variable referencing a [SketchArc](SketchArc.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"sketchArc\_var" is a variable referencing a [SketchArc](SketchArc.htm) object.  ```` ``` #include <Fusion/Sketch/SketchArc.h>  // Uses no optional arguments. returnValue = sketchArc_var->breakCurve(segmentPoint);  // Uses optional arguments. returnValue = sketchArc_var->breakCurve(segmentPoint, createConstraints); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | All of the curves resulting from the break are returned in an ObjectCollection. In the case where no intersections are found and as a result the curve is not broken, an empty ObjectCollection is returned. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| segmentPoint | [Point3D](Point3D.htm) | A point that specifies the segment of the curve that is to be split from the rest of the curve. The nearest intersection(s) to this point define the break location(s). |
| createConstraints | boolean | Optional argument that specifies if constraints should be created between the new curve segments. A value of true indicates constraints will be created.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchArcs.breakCurve](SketchArcs_breakCurve_Sample.htm) | Demonstrates the SketchArc.breakCurve method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |