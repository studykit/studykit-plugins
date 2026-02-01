# ClearanceHoleDataQuery.standardCustomName Method

Parent Object: [ClearanceHoleDataQuery](ClearanceHoleDataQuery.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ClearanceHoleDataQuery.h>

## Description

Method that returns the custom name for a given standard. The custom name is the localized name of the standard using the current language specified for Fusion.

## Syntax

* [Python](#Python)
* [C++](#C++)

"clearanceHoleDataQuery\_var" is a variable referencing a [ClearanceHoleDataQuery](ClearanceHoleDataQuery.htm) object.```` ``` returnValue = clearanceHoleDataQuery_var.standardCustomName(standard) ``` ```` |

"clearanceHoleDataQuery\_var" is a variable referencing a [ClearanceHoleDataQuery](ClearanceHoleDataQuery.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string | Returns the specified custom name or an empty string if an invalid standard is specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| standard | string | The standard you want to get the custom name for. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |