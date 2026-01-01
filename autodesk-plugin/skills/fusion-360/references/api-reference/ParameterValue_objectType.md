# ParameterValue.objectType Property

Parent Object: [ParameterValue](ParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/ParameterValue.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"parameterValue\_var" is a variable referencing a ParameterValue object.  ```` ``` # Get the value of the property. propertyValue = parameterValue_var.objectType ``` ```` |

"parameterValue\_var" is a variable referencing a ParameterValue object. ```` ``` #include <Cam/Operations/ParameterValue.h>  // Get the value of the property. string propertyValue = parameterValue_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |