# SketchOffsetDimension.objectType Property

Parent Object: [SketchOffsetDimension](SketchOffsetDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchOffsetDimension.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchOffsetDimension\_var" is a variable referencing a SketchOffsetDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchOffsetDimension_var.objectType ``` ```` |

"sketchOffsetDimension\_var" is a variable referencing a SketchOffsetDimension object. ```` ``` #include <Fusion/Sketch/SketchOffsetDimension.h>  // Get the value of the property. string propertyValue = sketchOffsetDimension_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |