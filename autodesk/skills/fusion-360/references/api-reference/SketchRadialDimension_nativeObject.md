# SketchRadialDimension.nativeObject Property

Parent Object: [SketchRadialDimension](SketchRadialDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchRadialDimension.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchRadialDimension\_var" is a variable referencing a SketchRadialDimension object. |

"sketchRadialDimension\_var" is a variable referencing a SketchRadialDimension object. ```` ``` #include <Fusion/Sketch/SketchRadialDimension.h>  // Get the value of the property. Ptr<SketchRadialDimension> propertyValue = sketchRadialDimension_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchRadialDimension](SketchRadialDimension.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |