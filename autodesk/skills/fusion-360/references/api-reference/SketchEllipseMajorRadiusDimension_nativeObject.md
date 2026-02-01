# SketchEllipseMajorRadiusDimension.nativeObject Property

Parent Object: [SketchEllipseMajorRadiusDimension](SketchEllipseMajorRadiusDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipseMajorRadiusDimension.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipseMajorRadiusDimension\_var" is a variable referencing a SketchEllipseMajorRadiusDimension object. |

"sketchEllipseMajorRadiusDimension\_var" is a variable referencing a SketchEllipseMajorRadiusDimension object. ```` ``` #include <Fusion/Sketch/SketchEllipseMajorRadiusDimension.h>  // Get the value of the property. Ptr<SketchEllipseMajorRadiusDimension> propertyValue = sketchEllipseMajorRadiusDimension_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchEllipseMajorRadiusDimension](SketchEllipseMajorRadiusDimension.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |