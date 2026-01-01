# JointGeometry.entityOne Property

Parent Object: [JointGeometry](JointGeometry.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointGeometry.h>

## Description

The first entity that's defining this joint geometry. This can be various types of geometry depending on how this joint geometry is defined. The geometryType property indicates how this joint geometry is defined a provides a clue about the type of geometry to expect back from this property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointGeometry\_var" is a variable referencing a JointGeometry object. |

"jointGeometry\_var" is a variable referencing a JointGeometry object. ```` ``` #include <Fusion/Components/JointGeometry.h>  // Get the value of the property. Ptr<Base> propertyValue = jointGeometry_var->entityOne(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |