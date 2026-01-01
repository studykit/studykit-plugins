# Operation.modifyUtility Method

Parent Object: [Operation](Operation.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operation.h>

## Description

Get ModifyUtility for the current operation by given utility type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operation\_var" is a variable referencing an [Operation](Operation.htm) object.```` ``` returnValue = operation_var.modifyUtility(utility) ``` ```` |

"operation\_var" is a variable referencing an [Operation](Operation.htm) object. |

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