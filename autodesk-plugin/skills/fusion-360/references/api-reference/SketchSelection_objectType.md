# SketchSelection.objectType Property

Parent Object: [SketchSelection](SketchSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/SketchSelection.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchSelection\_var" is a variable referencing a SketchSelection object.  ```` ``` # Get the value of the property. propertyValue = sketchSelection_var.objectType ``` ```` |

"sketchSelection\_var" is a variable referencing a SketchSelection object. ```` ``` #include <Cam/GeometrySelections/SketchSelection.h>  // Get the value of the property. string propertyValue = sketchSelection_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |