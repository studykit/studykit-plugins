# SketchPoint.objectType Property

Parent Object: [SketchPoint](SketchPoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPoint.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchPoint\_var" is a variable referencing a SketchPoint object.  ```` ``` # Get the value of the property. propertyValue = sketchPoint_var.objectType ``` ```` |

"sketchPoint\_var" is a variable referencing a SketchPoint object. ```` ``` #include <Fusion/Sketch/SketchPoint.h>  // Get the value of the property. string propertyValue = sketchPoint_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |