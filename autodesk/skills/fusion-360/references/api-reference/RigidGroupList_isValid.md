# RigidGroupList.isValid Property

Parent Object: [RigidGroupList](RigidGroupList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidGroupList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rigidGroupList\_var" is a variable referencing a RigidGroupList object. |

"rigidGroupList\_var" is a variable referencing a RigidGroupList object. ```` ``` #include <Fusion/Components/RigidGroupList.h>  // Get the value of the property. boolean propertyValue = rigidGroupList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |