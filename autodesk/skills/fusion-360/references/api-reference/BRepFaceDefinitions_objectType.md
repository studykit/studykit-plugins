# BRepFaceDefinitions.objectType Property

Parent Object: [BRepFaceDefinitions](BRepFaceDefinitions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFaceDefinitions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFaceDefinitions\_var" is a variable referencing a BRepFaceDefinitions object.  ```` ``` # Get the value of the property. propertyValue = bRepFaceDefinitions_var.objectType ``` ```` |

"bRepFaceDefinitions\_var" is a variable referencing a BRepFaceDefinitions object. ```` ``` #include <Fusion/BRep/BRepFaceDefinitions.h>  // Get the value of the property. string propertyValue = bRepFaceDefinitions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |