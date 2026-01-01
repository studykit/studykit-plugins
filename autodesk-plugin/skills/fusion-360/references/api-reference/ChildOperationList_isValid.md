# ChildOperationList.isValid Property

Parent Object: [ChildOperationList](ChildOperationList.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/ChildOperationList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"childOperationList\_var" is a variable referencing a ChildOperationList object. |

"childOperationList\_var" is a variable referencing a ChildOperationList object. ```` ``` #include <Cam/CAM/ChildOperationList.h>  // Get the value of the property. boolean propertyValue = childOperationList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |