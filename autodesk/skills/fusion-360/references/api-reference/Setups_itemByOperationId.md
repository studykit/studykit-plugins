# Setups.itemByOperationId Method

Parent Object: [Setups](Setups.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/Setups.h>

## Description

Returns the setup with the specified operation id.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setups\_var" is a variable referencing a [Setups](Setups.htm) object.```` ``` returnValue = setups_var.itemByOperationId(id) ``` ```` |

"setups\_var" is a variable referencing a [Setups](Setups.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Setup](Setup.htm) | Returns the specified setup or null in the case where there is no setup with the specified operation id. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | integer | The id of the operation. |

## Version

Introduced in version May 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |