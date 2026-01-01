# StringParameterValue.objectType Property

Parent Object: [StringParameterValue](StringParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/StringParameterValue.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stringParameterValue\_var" is a variable referencing a StringParameterValue object.  ```` ``` # Get the value of the property. propertyValue = stringParameterValue_var.objectType ``` ```` |

"stringParameterValue\_var" is a variable referencing a StringParameterValue object. ```` ``` #include <Cam/Operations/StringParameterValue.h>  // Get the value of the property. string propertyValue = stringParameterValue_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |