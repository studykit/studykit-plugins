# JointMotion.isValid Property

Parent Object: [JointMotion](JointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointMotion.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointMotion\_var" is a variable referencing a JointMotion object. |

"jointMotion\_var" is a variable referencing a JointMotion object. ```` ``` #include <Fusion/Components/JointMotion.h>  // Get the value of the property. boolean propertyValue = jointMotion_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |