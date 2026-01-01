# DataEvent.remove Method

Parent Object: [DataEvent](DataEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataEvent\_var" is a variable referencing a [DataEvent](DataEvent.htm) object.```` ``` returnValue = dataEvent_var.remove(handler) ``` ```` |

"dataEvent\_var" is a variable referencing a [DataEvent](DataEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [DataEventHandler](DataEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |