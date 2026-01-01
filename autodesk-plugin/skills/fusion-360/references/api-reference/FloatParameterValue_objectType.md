# FloatParameterValue.objectType Property

Parent Object: [FloatParameterValue](FloatParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/FloatParameterValue.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatParameterValue\_var" is a variable referencing a FloatParameterValue object.  ```` ``` # Get the value of the property. propertyValue = floatParameterValue_var.objectType ``` ```` |

"floatParameterValue\_var" is a variable referencing a FloatParameterValue object. ```` ``` #include <Cam/Operations/FloatParameterValue.h>  // Get the value of the property. string propertyValue = floatParameterValue_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |