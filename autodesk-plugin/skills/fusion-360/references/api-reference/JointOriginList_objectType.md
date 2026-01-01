# JointOriginList.objectType Property

Parent Object: [JointOriginList](JointOriginList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOriginList.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOriginList\_var" is a variable referencing a JointOriginList object.  ```` ``` # Get the value of the property. propertyValue = jointOriginList_var.objectType ``` ```` |

"jointOriginList\_var" is a variable referencing a JointOriginList object. ```` ``` #include <Fusion/Components/JointOriginList.h>  // Get the value of the property. string propertyValue = jointOriginList_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |