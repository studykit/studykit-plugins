# ToolbarControl.isVisible Property

Parent Object: [ToolbarControl](ToolbarControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarControl.h>

## Description

Gets or sets if this control is currently visible.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarControl\_var" is a variable referencing a ToolbarControl object. |

"toolbarControl\_var" is a variable referencing a ToolbarControl object. ```` ``` #include <Core/UserInterface/ToolbarControl.h>  // Get the value of the property. boolean propertyValue = toolbarControl_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = toolbarControl_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |