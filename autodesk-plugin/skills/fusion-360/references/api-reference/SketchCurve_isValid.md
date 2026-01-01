# SketchCurve.isValid Property

Parent Object: [SketchCurve](SketchCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurve.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCurve\_var" is a variable referencing a SketchCurve object. |

"sketchCurve\_var" is a variable referencing a SketchCurve object. ```` ``` #include <Fusion/Sketch/SketchCurve.h>  // Get the value of the property. boolean propertyValue = sketchCurve_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |