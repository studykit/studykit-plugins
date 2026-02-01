# SketchOffsetCurvesDimension.nativeObject Property

Parent Object: [SketchOffsetCurvesDimension](SketchOffsetCurvesDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchOffsetCurvesDimension.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchOffsetCurvesDimension\_var" is a variable referencing a SketchOffsetCurvesDimension object. |

"sketchOffsetCurvesDimension\_var" is a variable referencing a SketchOffsetCurvesDimension object. ```` ``` #include <Fusion/Sketch/SketchOffsetCurvesDimension.h>  // Get the value of the property. Ptr<SketchOffsetCurvesDimension> propertyValue = sketchOffsetCurvesDimension_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchOffsetCurvesDimension](SketchOffsetCurvesDimension.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |