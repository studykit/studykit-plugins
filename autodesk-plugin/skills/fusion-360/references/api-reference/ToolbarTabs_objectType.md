# ToolbarTabs.objectType Property

Parent Object: [ToolbarTabs](ToolbarTabs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarTabs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarTabs\_var" is a variable referencing a ToolbarTabs object.  ```` ``` # Get the value of the property. propertyValue = toolbarTabs_var.objectType ``` ```` |

"toolbarTabs\_var" is a variable referencing a ToolbarTabs object. ```` ``` #include <Core/UserInterface/ToolbarTabs.h>  // Get the value of the property. string propertyValue = toolbarTabs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |