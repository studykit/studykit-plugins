# ChildOperationList.objectType Property

Parent Object: [ChildOperationList](ChildOperationList.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/ChildOperationList.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"childOperationList\_var" is a variable referencing a ChildOperationList object.  ```` ``` # Get the value of the property. propertyValue = childOperationList_var.objectType ``` ```` |

"childOperationList\_var" is a variable referencing a ChildOperationList object. ```` ``` #include <Cam/CAM/ChildOperationList.h>  // Get the value of the property. string propertyValue = childOperationList_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |