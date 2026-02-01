# SketchLineList.isValid Property

Parent Object: [SketchLineList](SketchLineList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLineList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLineList\_var" is a variable referencing a SketchLineList object. |

"sketchLineList\_var" is a variable referencing a SketchLineList object. ```` ``` #include <Fusion/Sketch/SketchLineList.h>  // Get the value of the property. boolean propertyValue = sketchLineList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |