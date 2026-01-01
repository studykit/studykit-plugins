# CustomEvent.remove Method

Parent Object: [CustomEvent](CustomEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CustomEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customEvent\_var" is a variable referencing a [CustomEvent](CustomEvent.htm) object.```` ``` returnValue = customEvent_var.remove(handler) ``` ```` |

"customEvent\_var" is a variable referencing a [CustomEvent](CustomEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [CustomEventHandler](CustomEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |