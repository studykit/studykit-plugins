# BRepFaceDefinition.objectType Property

Parent Object: [BRepFaceDefinition](BRepFaceDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepFaceDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepFaceDefinition\_var" is a variable referencing a BRepFaceDefinition object.  ```` ``` # Get the value of the property. propertyValue = bRepFaceDefinition_var.objectType ``` ```` |

"bRepFaceDefinition\_var" is a variable referencing a BRepFaceDefinition object. ```` ``` #include <Fusion/BRep/BRepFaceDefinition.h>  // Get the value of the property. string propertyValue = bRepFaceDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |