# ToolbarTab.isValid Property

Parent Object: [ToolbarTab](ToolbarTab.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarTab.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarTab\_var" is a variable referencing a ToolbarTab object. |

"toolbarTab\_var" is a variable referencing a ToolbarTab object. ```` ``` #include <Core/UserInterface/ToolbarTab.h>  // Get the value of the property. boolean propertyValue = toolbarTab_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |