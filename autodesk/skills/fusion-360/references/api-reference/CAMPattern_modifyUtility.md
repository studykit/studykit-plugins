# CAMPattern.modifyUtility Method

Parent Object: [CAMPattern](CAMPattern.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMPattern.h>

## Description

Get ModifyUtility for the current operation by given utility type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMPattern\_var" is a variable referencing a [CAMPattern](CAMPattern.htm) object.```` ``` returnValue = cAMPattern_var.modifyUtility(utility) ``` ```` |

"cAMPattern\_var" is a variable referencing a [CAMPattern](CAMPattern.htm) object. |

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

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |