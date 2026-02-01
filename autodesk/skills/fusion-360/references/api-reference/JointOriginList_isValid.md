# JointOriginList.isValid Property

Parent Object: [JointOriginList](JointOriginList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOriginList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOriginList\_var" is a variable referencing a JointOriginList object. |

"jointOriginList\_var" is a variable referencing a JointOriginList object. ```` ``` #include <Fusion/Components/JointOriginList.h>  // Get the value of the property. boolean propertyValue = jointOriginList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |