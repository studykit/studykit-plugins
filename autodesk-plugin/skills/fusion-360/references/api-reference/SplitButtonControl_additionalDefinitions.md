# SplitButtonControl.additionalDefinitions Property

Parent Object: [SplitButtonControl](SplitButtonControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SplitButtonControl.h>

## Description

Gets or sets the command definitions used to define the buttons associated with the split button.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitButtonControl\_var" is a variable referencing a SplitButtonControl object. |

"splitButtonControl\_var" is a variable referencing a SplitButtonControl object. ```` ``` #include <Core/UserInterface/SplitButtonControl.h>  // Get the value of the property. std::vector<Ptr<CommandDefinition>> propertyValue = splitButtonControl_var->additionalDefinitions();  // Set the value of the property, where value_var is a CommandDefinition. bool returnValue = splitButtonControl_var->additionalDefinitions(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [CommandDefinition](CommandDefinition.htm).

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