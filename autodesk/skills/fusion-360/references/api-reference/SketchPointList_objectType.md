# SketchPointList.objectType Property

Parent Object: [SketchPointList](SketchPointList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPointList.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchPointList\_var" is a variable referencing a SketchPointList object.  ```` ``` # Get the value of the property. propertyValue = sketchPointList_var.objectType ``` ```` |

"sketchPointList\_var" is a variable referencing a SketchPointList object. ```` ``` #include <Fusion/Sketch/SketchPointList.h>  // Get the value of the property. string propertyValue = sketchPointList_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |