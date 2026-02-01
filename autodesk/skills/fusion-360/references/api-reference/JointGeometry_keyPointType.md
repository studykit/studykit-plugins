# JointGeometry.keyPointType Property

Parent Object: [JointGeometry](JointGeometry.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointGeometry.h>

## Description

Returns the keypoint type this JointGeometry is using.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointGeometry\_var" is a variable referencing a JointGeometry object. |

"jointGeometry\_var" is a variable referencing a JointGeometry object. ```` ``` #include <Fusion/Components/JointGeometry.h>  // Get the value of the property. JointKeyPointTypes propertyValue = jointGeometry_var->keyPointType(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointKeyPointTypes](JointKeyPointTypes.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |