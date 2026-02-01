# SketchFixedSplines.objectType Property

Parent Object: [SketchFixedSplines](SketchFixedSplines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchFixedSplines.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchFixedSplines\_var" is a variable referencing a SketchFixedSplines object.  ```` ``` # Get the value of the property. propertyValue = sketchFixedSplines_var.objectType ``` ```` |

"sketchFixedSplines\_var" is a variable referencing a SketchFixedSplines object. ```` ``` #include <Fusion/Sketch/SketchFixedSplines.h>  // Get the value of the property. string propertyValue = sketchFixedSplines_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |