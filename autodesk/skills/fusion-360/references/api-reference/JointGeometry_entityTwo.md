# JointGeometry.entityTwo Property

Parent Object: [JointGeometry](JointGeometry.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointGeometry.h>

## Description

This is the second entity that defines this joint geometry. This isn't used for all joint geometry types and will return null in the cases where it's not used. A second geometry is used in the case where the geometryType property returns JointProfileGeometry, JointPlanarBRepFaceGeometry, JointBetweenTwoFacesGeometry or JointByTwoEdgeIntersectionGeometry.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointGeometry\_var" is a variable referencing a JointGeometry object. |

"jointGeometry\_var" is a variable referencing a JointGeometry object. ```` ``` #include <Fusion/Components/JointGeometry.h>  // Get the value of the property. Ptr<Base> propertyValue = jointGeometry_var->entityTwo(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |