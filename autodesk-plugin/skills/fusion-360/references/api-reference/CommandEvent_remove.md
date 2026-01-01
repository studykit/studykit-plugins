# CommandEvent.remove Method

Parent Object: [CommandEvent](CommandEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandEvent.h>

## Description

Removes a handler from this event endpoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandEvent\_var" is a variable referencing a [CommandEvent](CommandEvent.htm) object.```` ``` returnValue = commandEvent_var.remove(handler) ``` ```` |

"commandEvent\_var" is a variable referencing a [CommandEvent](CommandEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the handler was found and removed from the set of event handlers. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [CommandEventHandler](CommandEventHandler.htm) | A CommandEventHandler that was previously added to this event with the add method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |