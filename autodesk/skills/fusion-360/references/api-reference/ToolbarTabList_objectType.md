# ToolbarTabList.objectType Property

Parent Object: [ToolbarTabList](ToolbarTabList.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarTabList.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarTabList\_var" is a variable referencing a ToolbarTabList object.  ```` ``` # Get the value of the property. propertyValue = toolbarTabList_var.objectType ``` ```` |

"toolbarTabList\_var" is a variable referencing a ToolbarTabList object. ```` ``` #include <Core/UserInterface/ToolbarTabList.h>  // Get the value of the property. string propertyValue = toolbarTabList_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |