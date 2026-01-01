# JointLimits.isValid Property

Parent Object: [JointLimits](JointLimits.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointLimits.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointLimits\_var" is a variable referencing a JointLimits object. |

"jointLimits\_var" is a variable referencing a JointLimits object. ```` ``` #include <Fusion/Components/JointLimits.h>  // Get the value of the property. boolean propertyValue = jointLimits_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |