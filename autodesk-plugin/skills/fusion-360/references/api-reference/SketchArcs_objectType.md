# SketchArcs.objectType Property

Parent Object: [SketchArcs](SketchArcs.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchArcs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchArcs\_var" is a variable referencing a SketchArcs object.  ```` ``` # Get the value of the property. propertyValue = sketchArcs_var.objectType ``` ```` |

"sketchArcs\_var" is a variable referencing a SketchArcs object. ```` ``` #include <Fusion/Sketch/SketchArcs.h>  // Get the value of the property. string propertyValue = sketchArcs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |