# JointGeometry.planeOne Property

Parent Object: [JointGeometry](JointGeometry.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointGeometry.h>

## Description

Returns the first plane for joint geometry that is defined between two planes. Returns null in all other cases.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointGeometry\_var" is a variable referencing a JointGeometry object. |

"jointGeometry\_var" is a variable referencing a JointGeometry object. ```` ``` #include <Fusion/Components/JointGeometry.h>  // Get the value of the property. Ptr<Base> propertyValue = jointGeometry_var->planeOne(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |