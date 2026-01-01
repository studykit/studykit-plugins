# SketchPoints.objectType Property

Parent Object: [SketchPoints](SketchPoints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchPoints.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchPoints\_var" is a variable referencing a SketchPoints object.  ```` ``` # Get the value of the property. propertyValue = sketchPoints_var.objectType ``` ```` |

"sketchPoints\_var" is a variable referencing a SketchPoints object. ```` ``` #include <Fusion/Sketch/SketchPoints.h>  // Get the value of the property. string propertyValue = sketchPoints_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |