# SketchOffsetCurvesDimension.objectType Property

Parent Object: [SketchOffsetCurvesDimension](SketchOffsetCurvesDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchOffsetCurvesDimension.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchOffsetCurvesDimension\_var" is a variable referencing a SketchOffsetCurvesDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchOffsetCurvesDimension_var.objectType ``` ```` |

"sketchOffsetCurvesDimension\_var" is a variable referencing a SketchOffsetCurvesDimension object. ```` ``` #include <Fusion/Sketch/SketchOffsetCurvesDimension.h>  // Get the value of the property. string propertyValue = sketchOffsetCurvesDimension_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |