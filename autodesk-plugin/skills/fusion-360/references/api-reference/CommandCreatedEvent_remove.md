# CommandCreatedEvent.remove Method

Parent Object: [CommandCreatedEvent](CommandCreatedEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandCreatedEvent.h>

## Description

Removes a handler from this event endpoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandCreatedEvent\_var" is a variable referencing a [CommandCreatedEvent](CommandCreatedEvent.htm) object.```` ``` returnValue = commandCreatedEvent_var.remove(handler) ``` ```` |

"commandCreatedEvent\_var" is a variable referencing a [CommandCreatedEvent](CommandCreatedEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the handler was found and removed from the set of event handlers. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [CommandCreatedEventHandler](CommandCreatedEventHandler.htm) | A CommandCreatedEventHandler that was previously added to this event with the add method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |