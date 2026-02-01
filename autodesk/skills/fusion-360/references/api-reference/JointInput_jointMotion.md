# JointInput.jointMotion Property

Parent Object: [JointInput](JointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointInput.h>

## Description

Returns an object derived from JointMotion that defines how the motion between the two joint geometries is defined.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointInput\_var" is a variable referencing a JointInput object. |

"jointInput\_var" is a variable referencing a JointInput object. ```` ``` #include <Fusion/Components/JointInput.h>  // Get the value of the property. Ptr<JointMotion> propertyValue = jointInput_var->jointMotion(); ``` ```` |

## Property Value

This is a read only property whose value is a [JointMotion](JointMotion.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |