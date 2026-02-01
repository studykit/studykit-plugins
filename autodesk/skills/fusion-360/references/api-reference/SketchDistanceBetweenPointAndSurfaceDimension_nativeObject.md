# SketchDistanceBetweenPointAndSurfaceDimension.nativeObject Property

Parent Object: [SketchDistanceBetweenPointAndSurfaceDimension](SketchDistanceBetweenPointAndSurfaceDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDistanceBetweenPointAndSurfaceDimension.h>

## Description

The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDistanceBetweenPointAndSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenPointAndSurfaceDimension object. |

"sketchDistanceBetweenPointAndSurfaceDimension\_var" is a variable referencing a SketchDistanceBetweenPointAndSurfaceDimension object. ```` ``` #include <Fusion/Sketch/SketchDistanceBetweenPointAndSurfaceDimension.h>  // Get the value of the property. Ptr<SketchDistanceBetweenPointAndSurfaceDimension> propertyValue = sketchDistanceBetweenPointAndSurfaceDimension_var->nativeObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchDistanceBetweenPointAndSurfaceDimension](SketchDistanceBetweenPointAndSurfaceDimension.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |