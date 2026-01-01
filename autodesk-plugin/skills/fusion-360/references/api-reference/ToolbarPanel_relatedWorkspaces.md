# ToolbarPanel.relatedWorkspaces Property

Parent Object: [ToolbarPanel](ToolbarPanel.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarPanel.h>

## Description

Gets or sets the set of workspaces that this panel is displayed for.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarPanel\_var" is a variable referencing a ToolbarPanel object. |

"toolbarPanel\_var" is a variable referencing a ToolbarPanel object. ```` ``` #include <Core/UserInterface/ToolbarPanel.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = toolbarPanel_var->relatedWorkspaces();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = toolbarPanel_var->relatedWorkspaces(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |