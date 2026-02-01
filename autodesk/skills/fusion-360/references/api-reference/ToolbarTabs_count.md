# ToolbarTabs.count Property

Parent Object: [ToolbarTabs](ToolbarTabs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarTabs.h>

## Description

Gets the number of ToolbarTabs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarTabs\_var" is a variable referencing a ToolbarTabs object. |

"toolbarTabs\_var" is a variable referencing a ToolbarTabs object. ```` ``` #include <Core/UserInterface/ToolbarTabs.h>  // Get the value of the property. uinteger propertyValue = toolbarTabs_var->count(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write user interface to a file API Sample](WriteUserInterfaceToFile_Sample.htm) | Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic [User-Interface Customization with Fusion's API](UserInterface_UM.htm) |

## Version

Introduced in version August 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |