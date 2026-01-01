# CAMArrangeParameterValue.parent Property

Parent Object: [CAMArrangeParameterValue](CAMArrangeParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CAMArrangeParameterValue.h>

## Description

Get the parameter object that the value is associated with.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMArrangeParameterValue\_var" is a variable referencing a CAMArrangeParameterValue object. |

"cAMArrangeParameterValue\_var" is a variable referencing a CAMArrangeParameterValue object. ```` ``` #include <Cam/Operations/CAMArrangeParameterValue.h>  // Get the value of the property. Ptr<Base> propertyValue = cAMArrangeParameterValue_var->parent(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |