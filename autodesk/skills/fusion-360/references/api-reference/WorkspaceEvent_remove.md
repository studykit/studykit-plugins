# WorkspaceEvent.remove Method

Parent Object: [WorkspaceEvent](WorkspaceEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/WorkspaceEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspaceEvent\_var" is a variable referencing a [WorkspaceEvent](WorkspaceEvent.htm) object.```` ``` returnValue = workspaceEvent_var.remove(handler) ``` ```` |

"workspaceEvent\_var" is a variable referencing a [WorkspaceEvent](WorkspaceEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [WorkspaceEventHandler](WorkspaceEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |