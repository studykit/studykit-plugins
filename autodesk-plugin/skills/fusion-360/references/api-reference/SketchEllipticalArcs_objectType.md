# SketchEllipticalArcs.objectType Property

Parent Object: [SketchEllipticalArcs](SketchEllipticalArcs.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchEllipticalArcs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchEllipticalArcs\_var" is a variable referencing a SketchEllipticalArcs object.  ```` ``` # Get the value of the property. propertyValue = sketchEllipticalArcs_var.objectType ``` ```` |

"sketchEllipticalArcs\_var" is a variable referencing a SketchEllipticalArcs object. ```` ``` #include <Fusion/Sketch/SketchEllipticalArcs.h>  // Get the value of the property. string propertyValue = sketchEllipticalArcs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |