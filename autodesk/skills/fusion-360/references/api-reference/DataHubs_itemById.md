# DataHubs.itemById Method

Parent Object: [DataHubs](DataHubs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataHubs.h>

## Description

Returns the hub specified using the ID of the hub.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataHubs\_var" is a variable referencing a [DataHubs](DataHubs.htm) object.```` ``` returnValue = dataHubs_var.itemById(id) ``` ```` |

"dataHubs\_var" is a variable referencing a [DataHubs](DataHubs.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DataHub](DataHub.htm) | Returns the hub or null if a hub with the specified ID is not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID of the hub to return. This is the same ID used by the APS Data Management API. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |