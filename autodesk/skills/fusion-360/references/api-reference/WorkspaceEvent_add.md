# WorkspaceEvent.add Method

Parent Object: [WorkspaceEvent](WorkspaceEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/WorkspaceEvent.h>

## Description

Add a handler to be notified when the event occurs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspaceEvent\_var" is a variable referencing a [WorkspaceEvent](WorkspaceEvent.htm) object.```` ``` returnValue = workspaceEvent_var.add(handler) ``` ```` |

"workspaceEvent\_var" is a variable referencing a [WorkspaceEvent](WorkspaceEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the addition of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [WorkspaceEventHandler](WorkspaceEventHandler.htm) | The handler object to be called when this event is fired. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |