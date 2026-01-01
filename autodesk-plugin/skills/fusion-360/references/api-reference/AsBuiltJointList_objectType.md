# AsBuiltJointList.objectType Property

Parent Object: [AsBuiltJointList](AsBuiltJointList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJointList.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJointList\_var" is a variable referencing an AsBuiltJointList object.  ```` ``` # Get the value of the property. propertyValue = asBuiltJointList_var.objectType ``` ```` |

"asBuiltJointList\_var" is a variable referencing an AsBuiltJointList object. ```` ``` #include <Fusion/Components/AsBuiltJointList.h>  // Get the value of the property. string propertyValue = asBuiltJointList_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |