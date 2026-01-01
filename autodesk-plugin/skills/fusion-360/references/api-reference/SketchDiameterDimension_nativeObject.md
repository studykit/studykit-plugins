# SketchDiameterDimension.nativeObject Property

Parent Object: [SketchDiameterDimension](SketchDiameterDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDiameterDimension.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDiameterDimension\_var" is a variable referencing a SketchDiameterDimension object. |

"sketchDiameterDimension\_var" is a variable referencing a SketchDiameterDimension object. ```` ``` #include <Fusion/Sketch/SketchDiameterDimension.h>  // Get the value of the property. Ptr<SketchDiameterDimension> propertyValue = sketchDiameterDimension_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchDiameterDimension](SketchDiameterDimension.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |