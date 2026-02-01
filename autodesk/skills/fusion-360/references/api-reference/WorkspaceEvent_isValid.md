# WorkspaceEvent.isValid Property

Parent Object: [WorkspaceEvent](WorkspaceEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/WorkspaceEvent.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspaceEvent\_var" is a variable referencing a WorkspaceEvent object. |

"workspaceEvent\_var" is a variable referencing a WorkspaceEvent object. ```` ``` #include <Core/UserInterface/WorkspaceEvent.h>  // Get the value of the property. boolean propertyValue = workspaceEvent_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |