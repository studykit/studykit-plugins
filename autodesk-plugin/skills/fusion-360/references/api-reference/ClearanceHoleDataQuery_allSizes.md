# ClearanceHoleDataQuery.allSizes Method

Parent Object: [ClearanceHoleDataQuery](ClearanceHoleDataQuery.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ClearanceHoleDataQuery.h>

## Description

This method returns an array of all the sizes for the given standard and fastener type. Valid standards and fastener types can be obtained using the allStandards and allFastenerTypes functions.

## Syntax

* [Python](#Python)
* [C++](#C++)

"clearanceHoleDataQuery\_var" is a variable referencing a [ClearanceHoleDataQuery](ClearanceHoleDataQuery.htm) object.```` ``` returnValue = clearanceHoleDataQuery_var.allSizes(standard, fastenerType) ``` ```` |

"clearanceHoleDataQuery\_var" is a variable referencing a [ClearanceHoleDataQuery](ClearanceHoleDataQuery.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string[] | Returns the specified sizes or empty array if an invalid standard or fastener type is specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| standard | string | The standard to search within. |
| fastenerType | string | The fastener type in the specified standard to search within. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |