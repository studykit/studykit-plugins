# SketchCurves.sketchFittedSplines Property

Parent Object: [SketchCurves](SketchCurves.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurves.h>

## Description

Returns the sketch splines collection associated with this sketch. This provides access to the existing sketch splines and supports the creation of new sketch splines.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCurves\_var" is a variable referencing a SketchCurves object. |

"sketchCurves\_var" is a variable referencing a SketchCurves object. ```` ``` #include <Fusion/Sketch/SketchCurves.h>  // Get the value of the property. Ptr<SketchFittedSplines> propertyValue = sketchCurves_var->sketchFittedSplines(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchFittedSplines](SketchFittedSplines.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchFittedSplines.add](SketchFittedSplines_add_Sample.htm) | Demonstrates the SketchFittedSplines.add method. |
| [Sketch spline through points creation and relative functions API Sample](SketchSplineThroughPoints_Sample.htm) | Create a sketch spline with points and use some operations for spline tangent handle & curvature handle. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |