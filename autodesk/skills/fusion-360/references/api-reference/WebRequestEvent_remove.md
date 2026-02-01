# WebRequestEvent.remove Method

Parent Object: [WebRequestEvent](WebRequestEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/WebRequestEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webRequestEvent\_var" is a variable referencing a [WebRequestEvent](WebRequestEvent.htm) object.```` ``` returnValue = webRequestEvent_var.remove(handler) ``` ```` |

"webRequestEvent\_var" is a variable referencing a [WebRequestEvent](WebRequestEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [WebRequestEventHandler](WebRequestEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |