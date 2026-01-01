# MachineParts.itemById Method

Parent Object: [MachineParts](MachineParts.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachineParts.h>

## Description

Get the part with the given ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machineParts\_var" is a variable referencing a [MachineParts](MachineParts.htm) object.```` ``` returnValue = machineParts_var.itemById(id) ``` ```` |

"machineParts\_var" is a variable referencing a [MachineParts](MachineParts.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MachinePart](MachinePart.htm) | Returns the MachinePart with the given ID, or null if the given ID does not match any part in the collection. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID for the part to get. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |