# SketchEntityList.objectType Property

Parent Object: [SketchEntityList](SketchEntityList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEntityList.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEntityList\_var" is a variable referencing a SketchEntityList object.  ```` ``` # Get the value of the property. propertyValue = sketchEntityList_var.objectType ``` ```` |

"sketchEntityList\_var" is a variable referencing a SketchEntityList object. ```` ``` #include <Fusion/Sketch/SketchEntityList.h>  // Get the value of the property. string propertyValue = sketchEntityList_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |