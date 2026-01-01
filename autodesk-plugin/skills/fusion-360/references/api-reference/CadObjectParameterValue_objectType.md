# CadObjectParameterValue.objectType Property

Parent Object: [CadObjectParameterValue](CadObjectParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CadObjectParameterValue.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cadObjectParameterValue\_var" is a variable referencing a CadObjectParameterValue object.  ```` ``` # Get the value of the property. propertyValue = cadObjectParameterValue_var.objectType ``` ```` |

"cadObjectParameterValue\_var" is a variable referencing a CadObjectParameterValue object. ```` ``` #include <Cam/Operations/CadObjectParameterValue.h>  // Get the value of the property. string propertyValue = cadObjectParameterValue_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |