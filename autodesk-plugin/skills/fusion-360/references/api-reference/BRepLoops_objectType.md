# BRepLoops.objectType Property

Parent Object: [BRepLoops](BRepLoops.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoops.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLoops\_var" is a variable referencing a BRepLoops object.  ```` ``` # Get the value of the property. propertyValue = bRepLoops_var.objectType ``` ```` |

"bRepLoops\_var" is a variable referencing a BRepLoops object. ```` ``` #include <Fusion/BRep/BRepLoops.h>  // Get the value of the property. string propertyValue = bRepLoops_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |