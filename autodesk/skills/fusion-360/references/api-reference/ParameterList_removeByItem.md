# ParameterList.removeByItem Method

Parent Object: [ParameterList](ParameterList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ParameterList.h>

## Description

Method that removes a parameter from the list by specifying the parameter (item) to remove

## Syntax

* [Python](#Python)
* [C++](#C++)

"parameterList\_var" is a variable referencing a [ParameterList](ParameterList.htm) object.```` ``` returnValue = parameterList_var.removeByItem(item) ``` ```` |

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
| item | [Parameter](Parameter.htm) | The parameter item to remove from the list |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |