# SketchPoint.nativeObject Property

Parent Object: [SketchPoint](SketchPoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPoint.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchPoint\_var" is a variable referencing a SketchPoint object. |

"sketchPoint\_var" is a variable referencing a SketchPoint object. ```` ``` #include <Fusion/Sketch/SketchPoint.h>  // Get the value of the property. Ptr<SketchPoint> propertyValue = sketchPoint_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchPoint](SketchPoint.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |