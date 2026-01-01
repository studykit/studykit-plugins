# ParameterList.removeByIndex Method

Parent Object: [ParameterList](ParameterList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ParameterList.h>

## Description

Method that removes a parameter from the list using the index of the item in the list Will fail if the list is read only.

## Syntax

* [Python](#Python)
* [C++](#C++)

"parameterList\_var" is a variable referencing a [ParameterList](ParameterList.htm) object.```` ``` returnValue = parameterList_var.removeByIndex(index) ``` ```` |

"parameterList\_var" is a variable referencing a [ParameterList](ParameterList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. This method will fail if the list is read-only |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the parameter to be removed from the list |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |