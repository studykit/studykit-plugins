# KeyboardEvent.remove Method

Parent Object: [KeyboardEvent](KeyboardEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/KeyboardEvent.h>

## Description

Removes a handler from this event endpoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"keyboardEvent\_var" is a variable referencing a [KeyboardEvent](KeyboardEvent.htm) object.```` ``` returnValue = keyboardEvent_var.remove(handler) ``` ```` |

"keyboardEvent\_var" is a variable referencing a [KeyboardEvent](KeyboardEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the handler was found and removed from the set of event handlers. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [KeyboardEventHandler](KeyboardEventHandler.htm) | A KeyboardEventHandler that was previously added to this event with the add method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |