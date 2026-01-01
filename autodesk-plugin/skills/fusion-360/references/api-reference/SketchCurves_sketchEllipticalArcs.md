# SketchCurves.sketchEllipticalArcs Property

Parent Object: [SketchCurves](SketchCurves.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurves.h>

## Description

Returns the sketch elliptical arcs collection associated with this sketch. This provides access to the existing sketch elliptical arcs and supports the creation of new sketch elliptical arcs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCurves\_var" is a variable referencing a SketchCurves object. |

"sketchCurves\_var" is a variable referencing a SketchCurves object. ```` ``` #include <Fusion/Sketch/SketchCurves.h>  // Get the value of the property. Ptr<SketchEllipticalArcs> propertyValue = sketchCurves_var->sketchEllipticalArcs(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchEllipticalArcs](SketchEllipticalArcs.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |