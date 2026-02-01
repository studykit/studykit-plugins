# SketchControlPointSplines.objectType Property

Parent Object: [SketchControlPointSplines](SketchControlPointSplines.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchControlPointSplines.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchControlPointSplines\_var" is a variable referencing a SketchControlPointSplines object.  ```` ``` # Get the value of the property. propertyValue = sketchControlPointSplines_var.objectType ``` ```` |

"sketchControlPointSplines\_var" is a variable referencing a SketchControlPointSplines object. ```` ``` #include <Fusion/Sketch/SketchControlPointSplines.h>  // Get the value of the property. string propertyValue = sketchControlPointSplines_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |