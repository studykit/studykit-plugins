# SketchFittedSplines.objectType Property

Parent Object: [SketchFittedSplines](SketchFittedSplines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFittedSplines.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFittedSplines\_var" is a variable referencing a SketchFittedSplines object.  ```` ``` # Get the value of the property. propertyValue = sketchFittedSplines_var.objectType ``` ```` |

"sketchFittedSplines\_var" is a variable referencing a SketchFittedSplines object. ```` ``` #include <Fusion/Sketch/SketchFittedSplines.h>  // Get the value of the property. string propertyValue = sketchFittedSplines_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |