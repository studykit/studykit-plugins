# BRepFaces.objectType Property

Parent Object: [BRepFaces](BRepFaces.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFaces.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFaces\_var" is a variable referencing a BRepFaces object.  ```` ``` # Get the value of the property. propertyValue = bRepFaces_var.objectType ``` ```` |

"bRepFaces\_var" is a variable referencing a BRepFaces object. ```` ``` #include <Fusion/BRep/BRepFaces.h>  // Get the value of the property. string propertyValue = bRepFaces_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |