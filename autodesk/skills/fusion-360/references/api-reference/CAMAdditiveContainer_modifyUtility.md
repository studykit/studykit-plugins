# CAMAdditiveContainer.modifyUtility Method

Parent Object: [CAMAdditiveContainer](CAMAdditiveContainer.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMAdditiveContainer.h>

## Description

Get ModifyUtility for the current operation by given utility type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMAdditiveContainer\_var" is a variable referencing a [CAMAdditiveContainer](CAMAdditiveContainer.htm) object.```` ``` returnValue = cAMAdditiveContainer_var.modifyUtility(utility) ``` ```` |

"cAMAdditiveContainer\_var" is a variable referencing a [CAMAdditiveContainer](CAMAdditiveContainer.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ModifyUtility](ModifyUtility.htm) | Returns ModifyUtility for specific type or null if the type is not compatible with the operation. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| utility | [ModifyUtilityTypes](ModifyUtilityTypes.htm) | Defines the specific ModifyUtility. |

## Version

Introduced in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |