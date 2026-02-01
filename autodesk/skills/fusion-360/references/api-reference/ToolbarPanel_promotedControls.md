# ToolbarPanel.promotedControls Property

Parent Object: [ToolbarPanel](ToolbarPanel.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarPanel.h>

## Description

Gets the controls in the panel that have been promoted. Promoted controls are the controls that are displayed within the panel.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarPanel\_var" is a variable referencing a ToolbarPanel object. |

"toolbarPanel\_var" is a variable referencing a ToolbarPanel object. ```` ``` #include <Core/UserInterface/ToolbarPanel.h>  // Get the value of the property. Ptr<ToolbarControlList> propertyValue = toolbarPanel_var->promotedControls(); ``` ```` |

## Property Value

This is a read only property whose value is a [ToolbarControlList](ToolbarControlList.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |