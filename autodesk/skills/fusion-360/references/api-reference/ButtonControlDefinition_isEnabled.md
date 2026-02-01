# ButtonControlDefinition.isEnabled Property

Parent Object: [ButtonControlDefinition](ButtonControlDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ButtonControlDefinition.h>

## Description

Gets or sets if this definition is enabled or not. This has the effect of enabling and disabling any associated controls.

## Syntax

* [Python](#Python)
* [C++](#C++)

"buttonControlDefinition\_var" is a variable referencing a ButtonControlDefinition object. |

"buttonControlDefinition\_var" is a variable referencing a ButtonControlDefinition object. ```` ``` #include <Core/UserInterface/ButtonControlDefinition.h>  // Get the value of the property. boolean propertyValue = buttonControlDefinition_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = buttonControlDefinition_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

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