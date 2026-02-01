# SketchLinearDiameterDimension.nativeObject Property

Parent Object: [SketchLinearDiameterDimension](SketchLinearDiameterDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLinearDiameterDimension.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLinearDiameterDimension\_var" is a variable referencing a SketchLinearDiameterDimension object. |

"sketchLinearDiameterDimension\_var" is a variable referencing a SketchLinearDiameterDimension object. ```` ``` #include <Fusion/Sketch/SketchLinearDiameterDimension.h>  // Get the value of the property. Ptr<SketchLinearDiameterDimension> propertyValue = sketchLinearDiameterDimension_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchLinearDiameterDimension](SketchLinearDiameterDimension.htm).

## Version

Introduced in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |