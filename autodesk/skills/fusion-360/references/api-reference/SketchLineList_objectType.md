# SketchLineList.objectType Property

Parent Object: [SketchLineList](SketchLineList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLineList.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLineList\_var" is a variable referencing a SketchLineList object.  ```` ``` # Get the value of the property. propertyValue = sketchLineList_var.objectType ``` ```` |

"sketchLineList\_var" is a variable referencing a SketchLineList object. ```` ``` #include <Fusion/Sketch/SketchLineList.h>  // Get the value of the property. string propertyValue = sketchLineList_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |