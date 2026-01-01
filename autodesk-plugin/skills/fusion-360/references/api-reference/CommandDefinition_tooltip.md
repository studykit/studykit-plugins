# CommandDefinition.tooltip Property

Parent Object: [CommandDefinition](CommandDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandDefinition.h>

## Description

Gets or sets the tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandDefinition\_var" is a variable referencing a CommandDefinition object.  ```` ``` # Get the value of the property. propertyValue = commandDefinition_var.tooltip  # Set the value of the property. commandDefinition_var.tooltip = propertyValue ``` ```` |

"commandDefinition\_var" is a variable referencing a CommandDefinition object. ```` ``` #include <Core/UserInterface/CommandDefinition.h>  // Get the value of the property. string propertyValue = commandDefinition_var->tooltip();  // Set the value of the property, where value_var is a string. bool returnValue = commandDefinition_var->tooltip(value_var); ``` ```` |

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