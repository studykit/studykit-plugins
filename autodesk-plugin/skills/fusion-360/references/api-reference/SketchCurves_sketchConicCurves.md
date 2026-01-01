# SketchCurves.sketchConicCurves Property

Parent Object: [SketchCurves](SketchCurves.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurves.h>

## Description

Returns the conic curves collection associated with this sketch. This provides access to the existing conic curves and supports the creation of new conic curves.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCurves\_var" is a variable referencing a SketchCurves object. |

"sketchCurves\_var" is a variable referencing a SketchCurves object. ```` ``` #include <Fusion/Sketch/SketchCurves.h>  // Get the value of the property. Ptr<SketchConicCurves> propertyValue = sketchCurves_var->sketchConicCurves(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchConicCurves](SketchConicCurves.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |