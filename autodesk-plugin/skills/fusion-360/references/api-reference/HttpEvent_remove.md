# HttpEvent.remove Method

Parent Object: [HttpEvent](HttpEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpEvent\_var" is a variable referencing a [HttpEvent](HttpEvent.htm) object.```` ``` returnValue = httpEvent_var.remove(handler) ``` ```` |

"httpEvent\_var" is a variable referencing a [HttpEvent](HttpEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [HttpEventHandler](HttpEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |