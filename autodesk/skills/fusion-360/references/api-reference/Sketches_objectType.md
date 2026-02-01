# Sketches.objectType Property

Parent Object: [Sketches](Sketches.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketches.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketches\_var" is a variable referencing a Sketches object.  ```` ``` # Get the value of the property. propertyValue = sketches_var.objectType ``` ```` |

"sketches\_var" is a variable referencing a Sketches object. ```` ``` #include <Fusion/Sketch/Sketches.h>  // Get the value of the property. string propertyValue = sketches_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |