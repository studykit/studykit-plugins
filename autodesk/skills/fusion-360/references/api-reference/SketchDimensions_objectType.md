# SketchDimensions.objectType Property

Parent Object: [SketchDimensions](SketchDimensions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchDimensions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchDimensions\_var" is a variable referencing a SketchDimensions object.  ```` ``` # Get the value of the property. propertyValue = sketchDimensions_var.objectType ``` ```` |

"sketchDimensions\_var" is a variable referencing a SketchDimensions object. ```` ``` #include <Fusion/Sketch/SketchDimensions.h>  // Get the value of the property. string propertyValue = sketchDimensions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |