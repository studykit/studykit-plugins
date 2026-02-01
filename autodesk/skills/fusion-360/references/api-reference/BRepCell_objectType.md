# BRepCell.objectType Property

Parent Object: [BRepCell](BRepCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BRepCell.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCell\_var" is a variable referencing a BRepCell object.  ```` ``` # Get the value of the property. propertyValue = bRepCell_var.objectType ``` ```` |

"bRepCell\_var" is a variable referencing a BRepCell object. ```` ``` #include <Fusion/Features/BRepCell.h>  // Get the value of the property. string propertyValue = bRepCell_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |