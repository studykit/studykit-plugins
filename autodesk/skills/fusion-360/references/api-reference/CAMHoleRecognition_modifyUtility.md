# CAMHoleRecognition.modifyUtility Method

Parent Object: [CAMHoleRecognition](CAMHoleRecognition.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMHoleRecognition.h>

## Description

Get ModifyUtility for the current operation by given utility type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMHoleRecognition\_var" is a variable referencing a [CAMHoleRecognition](CAMHoleRecognition.htm) object.```` ``` returnValue = cAMHoleRecognition_var.modifyUtility(utility) ``` ```` |

"cAMHoleRecognition\_var" is a variable referencing a [CAMHoleRecognition](CAMHoleRecognition.htm) object. |

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