# ToolbarControlList.isValid Property

Parent Object: [ToolbarControlList](ToolbarControlList.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarControlList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarControlList\_var" is a variable referencing a ToolbarControlList object. |

"toolbarControlList\_var" is a variable referencing a ToolbarControlList object. ```` ``` #include <Core/UserInterface/ToolbarControlList.h>  // Get the value of the property. boolean propertyValue = toolbarControlList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |