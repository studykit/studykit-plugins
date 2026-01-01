# ParameterList.add Method

Parent Object: [ParameterList](ParameterList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ParameterList.h>

## Description

Adds a parameter to the list. This does not create a new parameter, it adds an existing parameter to the list. Note that duplicates can exist in the list.

## Syntax

* [Python](#Python)
* [C++](#C++)

"parameterList\_var" is a variable referencing a [ParameterList](ParameterList.htm) object.```` ``` returnValue = parameterList_var.add(parameter) ``` ```` |

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
| parameter | [Parameter](Parameter.htm) | The existing parameter to add to the list |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |