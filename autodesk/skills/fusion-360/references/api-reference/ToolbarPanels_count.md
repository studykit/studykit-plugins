# ToolbarPanels.count Property

Parent Object: [ToolbarPanels](ToolbarPanels.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarPanels.h>

## Description

Gets the number of ToolbarPanels.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarPanels\_var" is a variable referencing a ToolbarPanels object. |

"toolbarPanels\_var" is a variable referencing a ToolbarPanels object. ```` ``` #include <Core/UserInterface/ToolbarPanels.h>  // Get the value of the property. uinteger propertyValue = toolbarPanels_var->count(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write user interface to a file API Sample](WriteUserInterfaceToFile_Sample.htm) | Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic [User-Interface Customization with Fusion's API](UserInterface_UM.htm) |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |