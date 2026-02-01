# JointGeometry.tangentFaceType Property

Parent Object: [JointGeometry](JointGeometry.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointGeometry.h>

## Description

Returns the tangent face type this JointGeometry is using.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointGeometry\_var" is a variable referencing a JointGeometry object. |

"jointGeometry\_var" is a variable referencing a JointGeometry object. ```` ``` #include <Fusion/Components/JointGeometry.h>  // Get the value of the property. JointTangentFaceTypes propertyValue = jointGeometry_var->tangentFaceType(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointTangentFaceTypes](JointTangentFaceTypes.htm).

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |