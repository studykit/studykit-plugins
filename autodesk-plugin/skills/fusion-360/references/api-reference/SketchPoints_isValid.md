# SketchPoints.isValid Property

Parent Object: [SketchPoints](SketchPoints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPoints.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchPoints\_var" is a variable referencing a SketchPoints object. |

"sketchPoints\_var" is a variable referencing a SketchPoints object. ```` ``` #include <Fusion/Sketch/SketchPoints.h>  // Get the value of the property. boolean propertyValue = sketchPoints_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |