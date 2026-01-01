# JointList.isValid Property

Parent Object: [JointList](JointList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointList\_var" is a variable referencing a JointList object. |

"jointList\_var" is a variable referencing a JointList object. ```` ``` #include <Fusion/Components/JointList.h>  // Get the value of the property. boolean propertyValue = jointList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |