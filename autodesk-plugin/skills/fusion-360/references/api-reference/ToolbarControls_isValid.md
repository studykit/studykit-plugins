# ToolbarControls.isValid Property

Parent Object: [ToolbarControls](ToolbarControls.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarControls.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarControls\_var" is a variable referencing a ToolbarControls object. |

"toolbarControls\_var" is a variable referencing a ToolbarControls object. ```` ``` #include <Core/UserInterface/ToolbarControls.h>  // Get the value of the property. boolean propertyValue = toolbarControls_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |