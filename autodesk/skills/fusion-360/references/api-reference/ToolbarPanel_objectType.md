# ToolbarPanel.objectType Property

Parent Object: [ToolbarPanel](ToolbarPanel.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarPanel.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarPanel\_var" is a variable referencing a ToolbarPanel object.  ```` ``` # Get the value of the property. propertyValue = toolbarPanel_var.objectType ``` ```` |

"toolbarPanel\_var" is a variable referencing a ToolbarPanel object. ```` ``` #include <Core/UserInterface/ToolbarPanel.h>  // Get the value of the property. string propertyValue = toolbarPanel_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |