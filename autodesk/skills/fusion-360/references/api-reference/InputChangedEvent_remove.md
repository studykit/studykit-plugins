# InputChangedEvent.remove Method

Parent Object: [InputChangedEvent](InputChangedEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/InputChangedEvent.h>

## Description

Removes a handler from this event endpoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"inputChangedEvent\_var" is a variable referencing an [InputChangedEvent](InputChangedEvent.htm) object.```` ``` returnValue = inputChangedEvent_var.remove(handler) ``` ```` |

"inputChangedEvent\_var" is a variable referencing an [InputChangedEvent](InputChangedEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the handler was found and removed from the set of event handlers. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [InputChangedEventHandler](InputChangedEventHandler.htm) | A InputChangedEventHandler that was previously added to this event with the add method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |