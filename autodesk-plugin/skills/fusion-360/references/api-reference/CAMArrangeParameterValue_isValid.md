# CAMArrangeParameterValue.isValid Property

Parent Object: [CAMArrangeParameterValue](CAMArrangeParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/CAMArrangeParameterValue.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMArrangeParameterValue\_var" is a variable referencing a CAMArrangeParameterValue object. |

"cAMArrangeParameterValue\_var" is a variable referencing a CAMArrangeParameterValue object. ```` ``` #include <Cam/Operations/CAMArrangeParameterValue.h>  // Get the value of the property. boolean propertyValue = cAMArrangeParameterValue_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |