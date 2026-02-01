# ApplicationEvent.remove Method

Parent Object: [ApplicationEvent](ApplicationEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ApplicationEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationEvent\_var" is a variable referencing an [ApplicationEvent](ApplicationEvent.htm) object.```` ``` returnValue = applicationEvent_var.remove(handler) ``` ```` |

"applicationEvent\_var" is a variable referencing an [ApplicationEvent](ApplicationEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [ApplicationEventHandler](ApplicationEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |