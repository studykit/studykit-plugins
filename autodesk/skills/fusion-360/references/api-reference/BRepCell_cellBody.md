# BRepCell.cellBody Property

Parent Object: [BRepCell](BRepCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BRepCell.h>

## Description

Returns a BRepBody that represents this cell. This is a transient B-Rep body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCell\_var" is a variable referencing a BRepCell object. |

"bRepCell\_var" is a variable referencing a BRepCell object. ```` ``` #include <Fusion/Features/BRepCell.h>  // Get the value of the property. Ptr<BRepBody> propertyValue = bRepCell_var->cellBody(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBody](BRepBody.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |