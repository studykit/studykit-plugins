# Command.parentCommandDefinition Property

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Gets the parent CommandDefinition object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"command\_var" is a variable referencing a Command object. |

"command\_var" is a variable referencing a Command object. ```` ``` #include <Core/UserInterface/Command.h>  // Get the value of the property. Ptr<CommandDefinition> propertyValue = command_var->parentCommandDefinition(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandDefinition](CommandDefinition.htm).

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