# ToolbarControls.count Property

Parent Object: [ToolbarControls](ToolbarControls.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ToolbarControls.h>

## Description

Gets the number of controls in the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbarControls\_var" is a variable referencing a ToolbarControls object. |

"toolbarControls\_var" is a variable referencing a ToolbarControls object. ```` ``` #include <Core/UserInterface/ToolbarControls.h>  // Get the value of the property. uinteger propertyValue = toolbarControls_var->count(); ``` ```` |

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