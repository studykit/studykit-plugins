# JointInput.isValid Property

Parent Object: [JointInput](JointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointInput.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointInput\_var" is a variable referencing a JointInput object. |

"jointInput\_var" is a variable referencing a JointInput object. ```` ``` #include <Fusion/Components/JointInput.h>  // Get the value of the property. boolean propertyValue = jointInput_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |