# SplitButtonControl.defaultCommandDefinition Property

Parent Object: [SplitButtonControl](SplitButtonControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SplitButtonControl.h>

## Description

Gets the command definition that is used as the default command on the main portion of the split button.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitButtonControl\_var" is a variable referencing a SplitButtonControl object. |

"splitButtonControl\_var" is a variable referencing a SplitButtonControl object. ```` ``` #include <Core/UserInterface/SplitButtonControl.h>  // Get the value of the property. Ptr<CommandDefinition> propertyValue = splitButtonControl_var->defaultCommandDefinition(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandDefinition](CommandDefinition.htm).

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