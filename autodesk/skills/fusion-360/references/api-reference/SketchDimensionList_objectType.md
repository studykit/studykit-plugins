# SketchDimensionList.objectType Property

Parent Object: [SketchDimensionList](SketchDimensionList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDimensionList.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDimensionList\_var" is a variable referencing a SketchDimensionList object.  ```` ``` # Get the value of the property. propertyValue = sketchDimensionList_var.objectType ``` ```` |

"sketchDimensionList\_var" is a variable referencing a SketchDimensionList object. ```` ``` #include <Fusion/Sketch/SketchDimensionList.h>  // Get the value of the property. string propertyValue = sketchDimensionList_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |