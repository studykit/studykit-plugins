# SketchLinearDimension.objectType Property

Parent Object: [SketchLinearDimension](SketchLinearDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchLinearDimension.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchLinearDimension\_var" is a variable referencing a SketchLinearDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchLinearDimension_var.objectType ``` ```` |

"sketchLinearDimension\_var" is a variable referencing a SketchLinearDimension object. ```` ``` #include <Fusion/Sketch/SketchLinearDimension.h>  // Get the value of the property. string propertyValue = sketchLinearDimension_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |