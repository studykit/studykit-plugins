# CommandDefinition.resourceFolder Property

Parent Object: [CommandDefinition](CommandDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandDefinition.h>

## Description

This argument defines the resource folder that contains the images used for the command icon. Icons can be defined using either PNG or SVG files. More information about icons can be found in the user manual topic [User Interface Customization](UserInterface_UM.htm#IconsForCommands).

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandDefinition\_var" is a variable referencing a CommandDefinition object. |

"commandDefinition\_var" is a variable referencing a CommandDefinition object. ```` ``` #include <Core/UserInterface/CommandDefinition.h>  // Get the value of the property. string propertyValue = commandDefinition_var->resourceFolder();  // Set the value of the property, where value_var is a string. bool returnValue = commandDefinition_var->resourceFolder(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Customizing the UI using the API Sample](UICustomizationSample_Sample.htm) | Demonstrates how to work with tabs, panels, and command in the user interface. The full source for [C++](../ExtraFiles/UICustomizationSampleCPP.zip) and [Python](../ExtraFiles/UICustomizationSamplePython.zip) samples can be downloaded. This is especially useful for getting the resource files. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |