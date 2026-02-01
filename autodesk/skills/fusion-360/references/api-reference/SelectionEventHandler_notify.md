# SelectionEventHandler.notify Method

Parent Object: [SelectionEventHandler](SelectionEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionEventHandler.h>

## Description

This notify member is called when an event is triggered from any event that this handler has been added to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionEventHandler\_var" is a variable referencing a [SelectionEventHandler](SelectionEventHandler.htm) object.```` ``` returnValue = selectionEventHandler_var.notify(eventArgs) ``` ```` |

"selectionEventHandler\_var" is a variable referencing a [SelectionEventHandler](SelectionEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [SelectionEventArgs](SelectionEventArgs.htm) | The arguments object with details about this event and the firing SelectionEvent. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |