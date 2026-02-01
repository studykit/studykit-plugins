# SketchEllipses.objectType Property

Parent Object: [SketchEllipses](SketchEllipses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipses.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipses\_var" is a variable referencing a SketchEllipses object.  ```` ``` # Get the value of the property. propertyValue = sketchEllipses_var.objectType ``` ```` |

"sketchEllipses\_var" is a variable referencing a SketchEllipses object. ```` ``` #include <Fusion/Sketch/SketchEllipses.h>  // Get the value of the property. string propertyValue = sketchEllipses_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |