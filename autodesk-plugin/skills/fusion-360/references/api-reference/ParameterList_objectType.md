# ParameterList.objectType Property

Parent Object: [ParameterList](ParameterList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ParameterList.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"parameterList\_var" is a variable referencing a ParameterList object.  ```` ``` # Get the value of the property. propertyValue = parameterList_var.objectType ``` ```` |

"parameterList\_var" is a variable referencing a ParameterList object. ```` ``` #include <Fusion/Fusion/ParameterList.h>  // Get the value of the property. string propertyValue = parameterList_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |