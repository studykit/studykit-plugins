# Toolbar.controls Property

Parent Object: [Toolbar](Toolbar.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Toolbar.h>

## Description

Gets the controls in this toolbar.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbar\_var" is a variable referencing a Toolbar object. |

"toolbar\_var" is a variable referencing a Toolbar object. ```` ``` #include <Core/UserInterface/Toolbar.h>  // Get the value of the property. Ptr<ToolbarControls> propertyValue = toolbar_var->controls(); ``` ```` |

## Property Value

This is a read only property whose value is a [ToolbarControls](ToolbarControls.htm).

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