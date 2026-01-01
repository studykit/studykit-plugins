# CommandDefinition.toolClipFilename Property

Parent Object: [CommandDefinition](CommandDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandDefinition.h>

## Description

Gets or sets the full filename of the image file (PNG) used for the tool clip. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip along with the tooltip text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandDefinition\_var" is a variable referencing a CommandDefinition object. |

"commandDefinition\_var" is a variable referencing a CommandDefinition object. ```` ``` #include <Core/UserInterface/CommandDefinition.h>  // Get the value of the property. string propertyValue = commandDefinition_var->toolClipFilename();  // Set the value of the property, where value_var is a string. bool returnValue = commandDefinition_var->toolClipFilename(value_var); ``` ```` |

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