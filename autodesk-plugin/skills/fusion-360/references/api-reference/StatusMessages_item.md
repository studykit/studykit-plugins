# StatusMessages.item Method

Parent Object: [StatusMessages](StatusMessages.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/StatusMessages.h>

## Description

Returns the specified status message using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"statusMessages\_var" is a variable referencing a [StatusMessages](StatusMessages.htm) object.```` ``` returnValue = statusMessages_var.item(index) ``` ```` |

"statusMessages\_var" is a variable referencing a [StatusMessages](StatusMessages.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [StatusMessage](StatusMessage.htm) | Returns the specified StatusMessage or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the status message within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |