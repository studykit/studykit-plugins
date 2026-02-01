# KeyboardEvent.add Method

Parent Object: [KeyboardEvent](KeyboardEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/KeyboardEvent.h>

## Description

Adds an event handler to this event endpoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"keyboardEvent\_var" is a variable referencing a [KeyboardEvent](KeyboardEvent.htm) object.```` ``` returnValue = keyboardEvent_var.add(handler) ``` ```` |

"keyboardEvent\_var" is a variable referencing a [KeyboardEvent](KeyboardEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the handler was successfully added to the set of event handlers. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [KeyboardEventHandler](KeyboardEventHandler.htm) | The client implemented KeyboardEventHandler to be called when this event is triggered. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |