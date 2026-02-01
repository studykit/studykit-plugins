# ToolbarTabList.isValid Property

Parent Object: [ToolbarTabList](ToolbarTabList.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarTabList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarTabList\_var" is a variable referencing a ToolbarTabList object. |

"toolbarTabList\_var" is a variable referencing a ToolbarTabList object. ```` ``` #include <Core/UserInterface/ToolbarTabList.h>  // Get the value of the property. boolean propertyValue = toolbarTabList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |