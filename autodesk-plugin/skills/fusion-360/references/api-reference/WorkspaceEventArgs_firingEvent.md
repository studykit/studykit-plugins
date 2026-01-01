# WorkspaceEventArgs.firingEvent Property

Parent Object: [WorkspaceEventArgs](WorkspaceEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/WorkspaceEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspaceEventArgs\_var" is a variable referencing a WorkspaceEventArgs object. |

"workspaceEventArgs\_var" is a variable referencing a WorkspaceEventArgs object. ```` ``` #include <Core/UserInterface/WorkspaceEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = workspaceEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |