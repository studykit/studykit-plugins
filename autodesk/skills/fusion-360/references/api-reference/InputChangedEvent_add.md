# InputChangedEvent.add Method

Parent Object: [InputChangedEvent](InputChangedEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/InputChangedEvent.h>

## Description

Adds an event handler to this event endpoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"inputChangedEvent\_var" is a variable referencing an [InputChangedEvent](InputChangedEvent.htm) object.```` ``` returnValue = inputChangedEvent_var.add(handler) ``` ```` |

"inputChangedEvent\_var" is a variable referencing an [InputChangedEvent](InputChangedEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the handler was successfully added to the set of event handlers. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [InputChangedEventHandler](InputChangedEventHandler.htm) | The client implemented InputChangedEventHandler to be called when this event is triggered. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |