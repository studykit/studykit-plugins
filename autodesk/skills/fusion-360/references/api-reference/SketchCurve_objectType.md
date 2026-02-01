# SketchCurve.objectType Property

Parent Object: [SketchCurve](SketchCurve.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurve.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCurve\_var" is a variable referencing a SketchCurve object.  ```` ``` # Get the value of the property. propertyValue = sketchCurve_var.objectType ``` ```` |

"sketchCurve\_var" is a variable referencing a SketchCurve object. ```` ``` #include <Fusion/Sketch/SketchCurve.h>  // Get the value of the property. string propertyValue = sketchCurve_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |