# SketchCurves.sketchFixedSplines Property

Parent Object: [SketchCurves](SketchCurves.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurves.h>

## Description

Returns the fixed sketch splines collection associated with this sketch. This provides access to the existing fixed sketch splines and supports the creation of new fixed sketch splines.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCurves\_var" is a variable referencing a SketchCurves object. |

"sketchCurves\_var" is a variable referencing a SketchCurves object. ```` ``` #include <Fusion/Sketch/SketchCurves.h>  // Get the value of the property. Ptr<SketchFixedSplines> propertyValue = sketchCurves_var->sketchFixedSplines(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchFixedSplines](SketchFixedSplines.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchFixedSplines.addByNurbsCurve](SketchFixedSplines_addByNurbsCurve_Sample.htm) | Demonstrates the SketchFixedSplines.addByNurbsCurve method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |