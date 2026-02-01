# CadObjectParameterValue.isValid Property

Parent Object: [CadObjectParameterValue](CadObjectParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CadObjectParameterValue.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cadObjectParameterValue\_var" is a variable referencing a CadObjectParameterValue object. |

"cadObjectParameterValue\_var" is a variable referencing a CadObjectParameterValue object. ```` ``` #include <Cam/Operations/CadObjectParameterValue.h>  // Get the value of the property. boolean propertyValue = cadObjectParameterValue_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |