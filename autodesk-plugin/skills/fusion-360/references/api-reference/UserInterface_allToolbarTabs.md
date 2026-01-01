# UserInterface.allToolbarTabs Property

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

Gets all of the toolbar tabs. This returns all of the tabs available, regardless of which workspace or product they're associated with.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterface\_var" is a variable referencing a UserInterface object. |

"userInterface\_var" is a variable referencing a UserInterface object. ```` ``` #include <Core/UserInterface/UserInterface.h>  // Get the value of the property. Ptr<ToolbarTabList> propertyValue = userInterface_var->allToolbarTabs(); ``` ```` |

## Property Value

This is a read only property whose value is a [ToolbarTabList](ToolbarTabList.htm).

## Version

Introduced in version August 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |