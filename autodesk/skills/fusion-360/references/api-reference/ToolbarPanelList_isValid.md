# ToolbarPanelList.isValid Property

Parent Object: [ToolbarPanelList](ToolbarPanelList.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarPanelList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarPanelList\_var" is a variable referencing a ToolbarPanelList object. |

"toolbarPanelList\_var" is a variable referencing a ToolbarPanelList object. ```` ``` #include <Core/UserInterface/ToolbarPanelList.h>  // Get the value of the property. boolean propertyValue = toolbarPanelList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |