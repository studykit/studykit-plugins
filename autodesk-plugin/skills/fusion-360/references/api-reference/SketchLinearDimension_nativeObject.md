# SketchLinearDimension.nativeObject Property

Parent Object: [SketchLinearDimension](SketchLinearDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLinearDimension.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLinearDimension\_var" is a variable referencing a SketchLinearDimension object. |

"sketchLinearDimension\_var" is a variable referencing a SketchLinearDimension object. ```` ``` #include <Fusion/Sketch/SketchLinearDimension.h>  // Get the value of the property. Ptr<SketchLinearDimension> propertyValue = sketchLinearDimension_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchLinearDimension](SketchLinearDimension.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |