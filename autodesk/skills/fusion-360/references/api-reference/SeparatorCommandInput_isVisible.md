# SeparatorCommandInput.isVisible Property

Parent Object: [SeparatorCommandInput](SeparatorCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SeparatorCommandInput.h>

## Description

Gets or sets if this input will be visible to the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"separatorCommandInput\_var" is a variable referencing a SeparatorCommandInput object.  ```` ``` # Get the value of the property. propertyValue = separatorCommandInput_var.isVisible  # Set the value of the property. separatorCommandInput_var.isVisible = propertyValue ``` ```` |

"separatorCommandInput\_var" is a variable referencing a SeparatorCommandInput object. ```` ``` #include <Core/UserInterface/SeparatorCommandInput.h>  // Get the value of the property. boolean propertyValue = separatorCommandInput_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = separatorCommandInput_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |