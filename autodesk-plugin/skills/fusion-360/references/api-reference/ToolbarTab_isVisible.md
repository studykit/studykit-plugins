# ToolbarTab.isVisible Property

Parent Object: [ToolbarTab](ToolbarTab.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarTab.h>

## Description

Gets or sets whether this tab is currently being displayed in the user interface. By default, a tab is made visible if it is associated with the active workspace and hidden otherwise. Setting it here will override that default behavior.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarTab\_var" is a variable referencing a ToolbarTab object. |

"toolbarTab\_var" is a variable referencing a ToolbarTab object. ```` ``` #include <Core/UserInterface/ToolbarTab.h>  // Get the value of the property. boolean propertyValue = toolbarTab_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = toolbarTab_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |