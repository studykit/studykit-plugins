# ApplicationEvent.add Method

Parent Object: [ApplicationEvent](ApplicationEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ApplicationEvent.h>

## Description

Add a handler to be notified when the event occurs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationEvent\_var" is a variable referencing an [ApplicationEvent](ApplicationEvent.htm) object.```` ``` returnValue = applicationEvent_var.add(handler) ``` ```` |

"applicationEvent\_var" is a variable referencing an [ApplicationEvent](ApplicationEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the addition of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [ApplicationEventHandler](ApplicationEventHandler.htm) | The handler object to be called when this event is fired. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |