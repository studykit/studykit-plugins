# ClearanceHoleDataQuery.allFastenerTypes Method

Parent Object: [ClearanceHoleDataQuery](ClearanceHoleDataQuery.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ClearanceHoleDataQuery.h>

## Description

This method returns an array of all the available fastener types for the given standard. To get the available standards, use the allStandards property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"clearanceHoleDataQuery\_var" is a variable referencing a [ClearanceHoleDataQuery](ClearanceHoleDataQuery.htm) object.```` ``` returnValue = clearanceHoleDataQuery_var.allFastenerTypes(standard) ``` ```` |

"clearanceHoleDataQuery\_var" is a variable referencing a [ClearanceHoleDataQuery](ClearanceHoleDataQuery.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string[] | Returns the specified fastener types or an empty array if an invalid standard is specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| standard | string | The standard to search within. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |