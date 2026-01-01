# BRepCell.isValid Property

Parent Object: [BRepCell](BRepCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BRepCell.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCell\_var" is a variable referencing a BRepCell object. |

"bRepCell\_var" is a variable referencing a BRepCell object. ```` ``` #include <Fusion/Features/BRepCell.h>  // Get the value of the property. boolean propertyValue = bRepCell_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |