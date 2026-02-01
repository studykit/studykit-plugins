# DataHubs.item Method

Parent Object: [DataHubs](DataHubs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataHubs.h>

## Description

Returns the specified hub.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataHubs\_var" is a variable referencing a [DataHubs](DataHubs.htm) object.```` ``` returnValue = dataHubs_var.item(index) ``` ```` |

"dataHubs\_var" is a variable referencing a [DataHubs](DataHubs.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DataHub](DataHub.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the hub to return. The first hub in the list has an index of 0. |

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |