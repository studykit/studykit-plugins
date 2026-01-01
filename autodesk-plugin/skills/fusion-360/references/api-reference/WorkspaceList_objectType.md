# WorkspaceList.objectType Property

Parent Object: [WorkspaceList](WorkspaceList.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/WorkspaceList.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspaceList\_var" is a variable referencing a WorkspaceList object.  ```` ``` # Get the value of the property. propertyValue = workspaceList_var.objectType ``` ```` |

"workspaceList\_var" is a variable referencing a WorkspaceList object. ```` ``` #include <Core/UserInterface/WorkspaceList.h>  // Get the value of the property. string propertyValue = workspaceList_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |