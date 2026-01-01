# SelectionEvent.add Method

Parent Object: [SelectionEvent](SelectionEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionEvent.h>

## Description

Adds an event handler to this event endpoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionEvent\_var" is a variable referencing a [SelectionEvent](SelectionEvent.htm) object.```` ``` returnValue = selectionEvent_var.add(handler) ``` ```` |

"selectionEvent\_var" is a variable referencing a [SelectionEvent](SelectionEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the handler was successfully added to the set of event handlers. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [SelectionEventHandler](SelectionEventHandler.htm) | The client implemented SelectionEventHandler to be called when this event is triggered. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |