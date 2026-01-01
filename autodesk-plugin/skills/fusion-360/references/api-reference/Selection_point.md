# Selection.point Property

Parent Object: [Selection](Selection.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Selection.h>

## Description

Gets the selection point on the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selection\_var" is a variable referencing a Selection object. |

"selection\_var" is a variable referencing a Selection object. ```` ``` #include <Core/UserInterface/Selection.h>  // Get the value of the property. Ptr<Point3D> propertyValue = selection_var->point(); ``` ```` |

## Property Value

This is a read only property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |