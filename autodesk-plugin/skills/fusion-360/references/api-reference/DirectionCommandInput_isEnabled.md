# DirectionCommandInput.isEnabled Property

Parent Object: [DirectionCommandInput](DirectionCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DirectionCommandInput.h>

## Description

Gets or sets if this input is currently enabled or disabled for user interaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"directionCommandInput\_var" is a variable referencing a DirectionCommandInput object.  ```` ``` # Get the value of the property. propertyValue = directionCommandInput_var.isEnabled  # Set the value of the property. directionCommandInput_var.isEnabled = propertyValue ``` ```` |

"directionCommandInput\_var" is a variable referencing a DirectionCommandInput object. ```` ``` #include <Core/UserInterface/DirectionCommandInput.h>  // Get the value of the property. boolean propertyValue = directionCommandInput_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = directionCommandInput_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |