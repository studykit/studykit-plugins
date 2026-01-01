# BooleanParameterValue.objectType Property

Parent Object: [BooleanParameterValue](BooleanParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/BooleanParameterValue.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"booleanParameterValue\_var" is a variable referencing a BooleanParameterValue object.  ```` ``` # Get the value of the property. propertyValue = booleanParameterValue_var.objectType ``` ```` |

"booleanParameterValue\_var" is a variable referencing a BooleanParameterValue object. ```` ``` #include <Cam/Operations/BooleanParameterValue.h>  // Get the value of the property. string propertyValue = booleanParameterValue_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |