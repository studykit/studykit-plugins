# CadContours2dParameterValue.parent Property

Parent Object: [CadContours2dParameterValue](CadContours2dParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CadContours2dParameterValue.h>

## Description

Get the parameter object that the value is associated with.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cadContours2dParameterValue\_var" is a variable referencing a CadContours2dParameterValue object. |

"cadContours2dParameterValue\_var" is a variable referencing a CadContours2dParameterValue object. ```` ``` #include <Cam/Operations/CadContours2dParameterValue.h>  // Get the value of the property. Ptr<Base> propertyValue = cadContours2dParameterValue_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |