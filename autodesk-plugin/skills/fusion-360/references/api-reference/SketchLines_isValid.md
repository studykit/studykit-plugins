# SketchLines.isValid Property

Parent Object: [SketchLines](SketchLines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLines.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLines\_var" is a variable referencing a SketchLines object. |

"sketchLines\_var" is a variable referencing a SketchLines object. ```` ``` #include <Fusion/Sketch/SketchLines.h>  // Get the value of the property. boolean propertyValue = sketchLines_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |