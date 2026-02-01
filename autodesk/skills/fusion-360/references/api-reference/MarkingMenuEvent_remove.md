# MarkingMenuEvent.remove Method

Parent Object: [MarkingMenuEvent](MarkingMenuEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MarkingMenuEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"markingMenuEvent\_var" is a variable referencing a [MarkingMenuEvent](MarkingMenuEvent.htm) object.```` ``` returnValue = markingMenuEvent_var.remove(handler) ``` ```` |

"markingMenuEvent\_var" is a variable referencing a [MarkingMenuEvent](MarkingMenuEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [MarkingMenuEventHandler](MarkingMenuEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |