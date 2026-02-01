# WorkspaceEventArgs.objectType Property

Parent Object: [WorkspaceEventArgs](WorkspaceEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/WorkspaceEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspaceEventArgs\_var" is a variable referencing a WorkspaceEventArgs object.  ```` ``` # Get the value of the property. propertyValue = workspaceEventArgs_var.objectType ``` ```` |

"workspaceEventArgs\_var" is a variable referencing a WorkspaceEventArgs object. ```` ``` #include <Core/UserInterface/WorkspaceEventArgs.h>  // Get the value of the property. string propertyValue = workspaceEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |