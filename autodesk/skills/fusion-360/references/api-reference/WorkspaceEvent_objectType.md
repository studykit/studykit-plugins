# WorkspaceEvent.objectType Property

Parent Object: [WorkspaceEvent](WorkspaceEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/WorkspaceEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspaceEvent\_var" is a variable referencing a WorkspaceEvent object.  ```` ``` # Get the value of the property. propertyValue = workspaceEvent_var.objectType ``` ```` |

"workspaceEvent\_var" is a variable referencing a WorkspaceEvent object. ```` ``` #include <Core/UserInterface/WorkspaceEvent.h>  // Get the value of the property. string propertyValue = workspaceEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |