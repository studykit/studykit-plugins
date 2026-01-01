# SketchCurves.sketchEllipses Property

Parent Object: [SketchCurves](SketchCurves.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurves.h>

## Description

Returns the sketch ellipses collection associated with this sketch. This provides access to the existing sketch ellipses and supports the creation of new sketch ellipses.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCurves\_var" is a variable referencing a SketchCurves object. |

"sketchCurves\_var" is a variable referencing a SketchCurves object. ```` ``` #include <Fusion/Sketch/SketchCurves.h>  // Get the value of the property. Ptr<SketchEllipses> propertyValue = sketchCurves_var->sketchEllipses(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchEllipses](SketchEllipses.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchEllipses.add](SketchEllipses_add_Sample.htm) | Demonstrates the SketchEllipses.add method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |