# Workspaces.objectType Property

Parent Object: [Workspaces](Workspaces.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Workspaces.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workspaces\_var" is a variable referencing a Workspaces object.  ```` ``` # Get the value of the property. propertyValue = workspaces_var.objectType ``` ```` |

"workspaces\_var" is a variable referencing a Workspaces object. ```` ``` #include <Core/UserInterface/Workspaces.h>  // Get the value of the property. string propertyValue = workspaces_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |