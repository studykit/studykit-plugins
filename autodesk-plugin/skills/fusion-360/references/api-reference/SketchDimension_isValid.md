# SketchDimension.isValid Property

Parent Object: [SketchDimension](SketchDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDimension.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDimension\_var" is a variable referencing a SketchDimension object. |

"sketchDimension\_var" is a variable referencing a SketchDimension object. ```` ``` #include <Fusion/Sketch/SketchDimension.h>  // Get the value of the property. boolean propertyValue = sketchDimension_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |