# BRepCell.sourceTools Property

Parent Object: [BRepCell](BRepCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BRepCell.h>

## Description

Returns the tools that we're using in the definition of this cell.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepCell\_var" is a variable referencing a BRepCell object. |

"bRepCell\_var" is a variable referencing a BRepCell object. ```` ``` #include <Fusion/Features/BRepCell.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = bRepCell_var->sourceTools(); ``` ```` |

## Property Value

This is a read only property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |