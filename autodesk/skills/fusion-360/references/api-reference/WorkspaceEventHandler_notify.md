# WorkspaceEventHandler.notify Method

Parent Object: [WorkspaceEventHandler](WorkspaceEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/WorkspaceEventHandler.h>

## Description

The function called by Fusion when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspaceEventHandler\_var" is a variable referencing a [WorkspaceEventHandler](WorkspaceEventHandler.htm) object.```` ``` returnValue = workspaceEventHandler_var.notify(eventArgs) ``` ```` |

"workspaceEventHandler\_var" is a variable referencing a [WorkspaceEventHandler](WorkspaceEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [WorkspaceEventArgs](WorkspaceEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |