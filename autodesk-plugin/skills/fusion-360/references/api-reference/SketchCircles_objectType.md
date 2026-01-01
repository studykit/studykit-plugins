# SketchCircles.objectType Property

Parent Object: [SketchCircles](SketchCircles.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCircles.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCircles\_var" is a variable referencing a SketchCircles object.  ```` ``` # Get the value of the property. propertyValue = sketchCircles_var.objectType ``` ```` |

"sketchCircles\_var" is a variable referencing a SketchCircles object. ```` ``` #include <Fusion/Sketch/SketchCircles.h>  // Get the value of the property. string propertyValue = sketchCircles_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |