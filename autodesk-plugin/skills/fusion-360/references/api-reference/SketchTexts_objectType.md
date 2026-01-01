# SketchTexts.objectType Property

Parent Object: [SketchTexts](SketchTexts.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTexts.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTexts\_var" is a variable referencing a SketchTexts object.  ```` ``` # Get the value of the property. propertyValue = sketchTexts_var.objectType ``` ```` |

"sketchTexts\_var" is a variable referencing a SketchTexts object. ```` ``` #include <Fusion/Sketch/SketchTexts.h>  // Get the value of the property. string propertyValue = sketchTexts_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |