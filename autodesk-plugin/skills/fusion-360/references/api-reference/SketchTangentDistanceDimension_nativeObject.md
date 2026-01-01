# SketchTangentDistanceDimension.nativeObject Property

Parent Object: [SketchTangentDistanceDimension](SketchTangentDistanceDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTangentDistanceDimension.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTangentDistanceDimension\_var" is a variable referencing a SketchTangentDistanceDimension object. |

"sketchTangentDistanceDimension\_var" is a variable referencing a SketchTangentDistanceDimension object. ```` ``` #include <Fusion/Sketch/SketchTangentDistanceDimension.h>  // Get the value of the property. Ptr<SketchTangentDistanceDimension> propertyValue = sketchTangentDistanceDimension_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchTangentDistanceDimension](SketchTangentDistanceDimension.htm).

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |