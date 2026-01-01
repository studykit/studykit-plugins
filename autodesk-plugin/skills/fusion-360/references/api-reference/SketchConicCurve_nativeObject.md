# SketchConicCurve.nativeObject Property

Parent Object: [SketchConicCurve](SketchConicCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchConicCurve.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchConicCurve\_var" is a variable referencing a SketchConicCurve object. |

"sketchConicCurve\_var" is a variable referencing a SketchConicCurve object. ```` ``` #include <Fusion/Sketch/SketchConicCurve.h>  // Get the value of the property. Ptr<SketchConicCurve> propertyValue = sketchConicCurve_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchConicCurve](SketchConicCurve.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |