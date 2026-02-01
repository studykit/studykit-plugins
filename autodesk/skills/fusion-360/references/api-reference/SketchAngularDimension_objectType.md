# SketchAngularDimension.objectType Property

Parent Object: [SketchAngularDimension](SketchAngularDimension.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchAngularDimension.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchAngularDimension\_var" is a variable referencing a SketchAngularDimension object.  ```` ``` # Get the value of the property. propertyValue = sketchAngularDimension_var.objectType ``` ```` |

"sketchAngularDimension\_var" is a variable referencing a SketchAngularDimension object. ```` ``` #include <Fusion/Sketch/SketchAngularDimension.h>  // Get the value of the property. string propertyValue = sketchAngularDimension_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |