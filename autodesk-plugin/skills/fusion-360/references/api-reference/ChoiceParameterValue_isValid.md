# ChoiceParameterValue.isValid Property

Parent Object: [ChoiceParameterValue](ChoiceParameterValue.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/ChoiceParameterValue.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"choiceParameterValue\_var" is a variable referencing a ChoiceParameterValue object. |

"choiceParameterValue\_var" is a variable referencing a ChoiceParameterValue object. ```` ``` #include <Cam/Operations/ChoiceParameterValue.h>  // Get the value of the property. boolean propertyValue = choiceParameterValue_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |