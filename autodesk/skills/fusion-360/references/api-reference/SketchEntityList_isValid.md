# SketchEntityList.isValid Property

Parent Object: [SketchEntityList](SketchEntityList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEntityList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEntityList\_var" is a variable referencing a SketchEntityList object. |

"sketchEntityList\_var" is a variable referencing a SketchEntityList object. ```` ``` #include <Fusion/Sketch/SketchEntityList.h>  // Get the value of the property. boolean propertyValue = sketchEntityList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |