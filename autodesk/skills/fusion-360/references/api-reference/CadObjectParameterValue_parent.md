# CadObjectParameterValue.parent Property

Parent Object: [CadObjectParameterValue](CadObjectParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CadObjectParameterValue.h>

## Description

Get the parameter object that the value is associated with.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cadObjectParameterValue\_var" is a variable referencing a CadObjectParameterValue object. |

"cadObjectParameterValue\_var" is a variable referencing a CadObjectParameterValue object. ```` ``` #include <Cam/Operations/CadObjectParameterValue.h>  // Get the value of the property. Ptr<Base> propertyValue = cadObjectParameterValue_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |