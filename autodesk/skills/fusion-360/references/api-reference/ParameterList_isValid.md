# ParameterList.isValid Property

Parent Object: [ParameterList](ParameterList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ParameterList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"parameterList\_var" is a variable referencing a ParameterList object. |

"parameterList\_var" is a variable referencing a ParameterList object. ```` ``` #include <Fusion/Fusion/ParameterList.h>  // Get the value of the property. boolean propertyValue = parameterList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |