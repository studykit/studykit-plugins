# BRepCells.objectType Property

Parent Object: [BRepCells](BRepCells.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BRepCells.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCells\_var" is a variable referencing a BRepCells object.  ```` ``` # Get the value of the property. propertyValue = bRepCells_var.objectType ``` ```` |

"bRepCells\_var" is a variable referencing a BRepCells object. ```` ``` #include <Fusion/Features/BRepCells.h>  // Get the value of the property. string propertyValue = bRepCells_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |