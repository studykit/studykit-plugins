# ToolbarPanel.isVisible Property

Parent Object: [ToolbarPanel](ToolbarPanel.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarPanel.h>

## Description

Gets or sets whether this panel is currently being displayed in the user interface. Visibility of a panel is controlled by it being associated with the currently active workspace. Setting it here will override that default behavior.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarPanel\_var" is a variable referencing a ToolbarPanel object. |

"toolbarPanel\_var" is a variable referencing a ToolbarPanel object. ```` ``` #include <Core/UserInterface/ToolbarPanel.h>  // Get the value of the property. boolean propertyValue = toolbarPanel_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = toolbarPanel_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |