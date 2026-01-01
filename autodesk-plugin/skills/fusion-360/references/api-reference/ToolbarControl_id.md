# ToolbarControl.id Property

Parent Object: [ToolbarControl](ToolbarControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarControl.h>

## Description

Gets the unique ID of this control. The ID is unique with respect to the other controls within the same panel, toolbar, or drop-down control.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarControl\_var" is a variable referencing a ToolbarControl object. |

"toolbarControl\_var" is a variable referencing a ToolbarControl object. ```` ``` #include <Core/UserInterface/ToolbarControl.h>  // Get the value of the property. string propertyValue = toolbarControl_var->id(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |