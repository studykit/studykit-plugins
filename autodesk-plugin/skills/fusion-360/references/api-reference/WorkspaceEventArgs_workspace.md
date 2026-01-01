# WorkspaceEventArgs.workspace Property

Parent Object: [WorkspaceEventArgs](WorkspaceEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/WorkspaceEventArgs.h>

## Description

Provides access to the workspace.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspaceEventArgs\_var" is a variable referencing a WorkspaceEventArgs object. |

"workspaceEventArgs\_var" is a variable referencing a WorkspaceEventArgs object. ```` ``` #include <Core/UserInterface/WorkspaceEventArgs.h>  // Get the value of the property. Ptr<Workspace> propertyValue = workspaceEventArgs_var->workspace(); ``` ```` |

## Property Value

This is a read only property whose value is a [Workspace](Workspace.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |