# ActiveSelectionEvent.remove Method

Parent Object: [ActiveSelectionEvent](ActiveSelectionEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ActiveSelectionEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"activeSelectionEvent\_var" is a variable referencing an [ActiveSelectionEvent](ActiveSelectionEvent.htm) object.```` ``` returnValue = activeSelectionEvent_var.remove(handler) ``` ```` |

"activeSelectionEvent\_var" is a variable referencing an [ActiveSelectionEvent](ActiveSelectionEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [ActiveSelectionEventHandler](ActiveSelectionEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |