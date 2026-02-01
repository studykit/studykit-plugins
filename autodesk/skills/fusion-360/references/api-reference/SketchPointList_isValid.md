# SketchPointList.isValid Property

Parent Object: [SketchPointList](SketchPointList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPointList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchPointList\_var" is a variable referencing a SketchPointList object. |

"sketchPointList\_var" is a variable referencing a SketchPointList object. ```` ``` #include <Fusion/Sketch/SketchPointList.h>  // Get the value of the property. boolean propertyValue = sketchPointList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |