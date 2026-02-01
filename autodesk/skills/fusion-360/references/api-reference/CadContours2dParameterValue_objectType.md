# CadContours2dParameterValue.objectType Property

Parent Object: [CadContours2dParameterValue](CadContours2dParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CadContours2dParameterValue.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cadContours2dParameterValue\_var" is a variable referencing a CadContours2dParameterValue object.  ```` ``` # Get the value of the property. propertyValue = cadContours2dParameterValue_var.objectType ``` ```` |

"cadContours2dParameterValue\_var" is a variable referencing a CadContours2dParameterValue object. ```` ``` #include <Cam/Operations/CadContours2dParameterValue.h>  // Get the value of the property. string propertyValue = cadContours2dParameterValue_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |