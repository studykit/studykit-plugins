# HttpEvent.add Method

Parent Object: [HttpEvent](HttpEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpEvent.h>

## Description

Add a handler to be notified when the event occurs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpEvent\_var" is a variable referencing a [HttpEvent](HttpEvent.htm) object.```` ``` returnValue = httpEvent_var.add(handler) ``` ```` |

"httpEvent\_var" is a variable referencing a [HttpEvent](HttpEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the addition of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [HttpEventHandler](HttpEventHandler.htm) | The handler object to be called when this event is fired. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |