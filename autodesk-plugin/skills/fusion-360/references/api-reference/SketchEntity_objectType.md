# SketchEntity.objectType Property

Parent Object: [SketchEntity](SketchEntity.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEntity.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEntity\_var" is a variable referencing a SketchEntity object.  ```` ``` # Get the value of the property. propertyValue = sketchEntity_var.objectType ``` ```` |

"sketchEntity\_var" is a variable referencing a SketchEntity object. ```` ``` #include <Fusion/Sketch/SketchEntity.h>  // Get the value of the property. string propertyValue = sketchEntity_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |