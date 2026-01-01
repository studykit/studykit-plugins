# ActiveSelectionEvent.add Method

Parent Object: [ActiveSelectionEvent](ActiveSelectionEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ActiveSelectionEvent.h>

## Description

Add a handler to be notified when the event occurs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"activeSelectionEvent\_var" is a variable referencing an [ActiveSelectionEvent](ActiveSelectionEvent.htm) object.```` ``` returnValue = activeSelectionEvent_var.add(handler) ``` ```` |

"activeSelectionEvent\_var" is a variable referencing an [ActiveSelectionEvent](ActiveSelectionEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the addition of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [ActiveSelectionEventHandler](ActiveSelectionEventHandler.htm) | The handler object to be called when this event is fired. |

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |