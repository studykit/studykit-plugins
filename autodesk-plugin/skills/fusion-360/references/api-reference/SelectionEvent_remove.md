# SelectionEvent.remove Method

Parent Object: [SelectionEvent](SelectionEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionEvent.h>

## Description

Removes a handler from this event endpoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionEvent\_var" is a variable referencing a [SelectionEvent](SelectionEvent.htm) object.```` ``` returnValue = selectionEvent_var.remove(handler) ``` ```` |

"selectionEvent\_var" is a variable referencing a [SelectionEvent](SelectionEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the handler was found and removed from the set of event handlers. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [SelectionEventHandler](SelectionEventHandler.htm) | A SelectionEventHandler that was previously added to this event with the add method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |