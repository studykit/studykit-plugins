# SketchCurves.sketchControlPointSplines Property

Parent Object: [SketchCurves](SketchCurves.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurves.h>

## Description

Returns the control point splines collection associated with this sketch. This provides access to the existing control point splines and supports the creation of new control point splines.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCurves\_var" is a variable referencing a SketchCurves object. |

"sketchCurves\_var" is a variable referencing a SketchCurves object. ```` ``` #include <Fusion/Sketch/SketchCurves.h>  // Get the value of the property. Ptr<SketchControlPointSplines> propertyValue = sketchCurves_var->sketchControlPointSplines(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchControlPointSplines](SketchControlPointSplines.htm).

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |