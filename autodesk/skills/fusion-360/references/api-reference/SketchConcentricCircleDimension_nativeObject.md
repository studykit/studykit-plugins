# SketchConcentricCircleDimension.nativeObject Property

Parent Object: [SketchConcentricCircleDimension](SketchConcentricCircleDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchConcentricCircleDimension.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchConcentricCircleDimension\_var" is a variable referencing a SketchConcentricCircleDimension object. |

"sketchConcentricCircleDimension\_var" is a variable referencing a SketchConcentricCircleDimension object. ```` ``` #include <Fusion/Sketch/SketchConcentricCircleDimension.h>  // Get the value of the property. Ptr<SketchConcentricCircleDimension> propertyValue = sketchConcentricCircleDimension_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchConcentricCircleDimension](SketchConcentricCircleDimension.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |