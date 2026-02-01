# ParameterList.find Method

Parent Object: [ParameterList](ParameterList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ParameterList.h>

## Description

Finds the specified parameter in the list. The search can be started at a specified index rather than from the beginning of the list. If not found, -1 is returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"parameterList\_var" is a variable referencing a [ParameterList](ParameterList.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"parameterList\_var" is a variable referencing a [ParameterList](ParameterList.htm) object.  ```` ``` #include <Fusion/Fusion/ParameterList.h>  // Uses no optional arguments. returnValue = parameterList_var->find(parameter);  // Uses optional arguments. returnValue = parameterList_var->find(parameter, startIndex); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| integer | Returns the index of the parameter found in the list. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| parameter | [Parameter](Parameter.htm) | The parameter to find |
| startIndex | uinteger | the index in the list to start the search from   This is an optional argument whose default value is 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |