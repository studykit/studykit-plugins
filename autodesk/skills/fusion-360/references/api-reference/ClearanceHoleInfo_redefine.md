# ClearanceHoleInfo.redefine Method

Parent Object: [ClearanceHoleInfo](ClearanceHoleInfo.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ClearanceHoleInfo.h>

## Description

Method that redefines the values associated with an existing ClearanceHoleInfo object. This is done to modify an existing clearance hole. The ClearanceHoleInfo object defines the type, size, and fit of the clearance hole to create. Fusion uses this information to look up the full details of the clearance hole in tables delivered with Fusion. The ClearanceHoleDataQuery object can be used to determine valid input for this information.

## Syntax

* [Python](#Python)
* [C++](#C++)

"clearanceHoleInfo\_var" is a variable referencing a [ClearanceHoleInfo](ClearanceHoleInfo.htm) object.```` ``` returnValue = clearanceHoleInfo_var.redefine(standard, fastenerType, size, fit) ``` ```` |

"clearanceHoleInfo\_var" is a variable referencing a [ClearanceHoleInfo](ClearanceHoleInfo.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| standard | string | Input string that specifies the standard. |
| fastenerType | string | Input string that specifies the fastener type. |
| size | string | Input string that specifies the fastener size. |
| fit | [ClearanceHoleFits](ClearanceHoleFits.htm) | Input enum value that specifies the amount of clearance between the hole and the fastener. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |