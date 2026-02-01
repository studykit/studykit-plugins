# DropDownControl.controls Property

Parent Object: [DropDownControl](DropDownControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DropDownControl.h>

## Description

Gets the associated ToolbarControls collection. Through this you can add additional controls to the drop-down.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dropDownControl\_var" is a variable referencing a DropDownControl object. |

"dropDownControl\_var" is a variable referencing a DropDownControl object. ```` ``` #include <Core/UserInterface/DropDownControl.h>  // Get the value of the property. Ptr<ToolbarControls> propertyValue = dropDownControl_var->controls(); ``` ```` |

## Property Value

This is a read only property whose value is a [ToolbarControls](ToolbarControls.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Customizing the UI using the API Sample](UICustomizationSample_Sample.htm) | Demonstrates how to work with tabs, panels, and command in the user interface. The full source for [C++](../ExtraFiles/UICustomizationSampleCPP.zip) and [Python](../ExtraFiles/UICustomizationSamplePython.zip) samples can be downloaded. This is especially useful for getting the resource files. |
| [Write user interface to a file API Sample](WriteUserInterfaceToFile_Sample.htm) | Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic [User-Interface Customization with Fusion's API](UserInterface_UM.htm) |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |