# AngleValueCommandInput.isEnabled Property

Parent Object: [AngleValueCommandInput](AngleValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/AngleValueCommandInput.h>

## Description

Gets or sets if this input is currently enabled or disabled for user interaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object.  ```` ``` # Get the value of the property. propertyValue = angleValueCommandInput_var.isEnabled  # Set the value of the property. angleValueCommandInput_var.isEnabled = propertyValue ``` ```` |

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object. ```` ``` #include <Core/UserInterface/AngleValueCommandInput.h>  // Get the value of the property. boolean propertyValue = angleValueCommandInput_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = angleValueCommandInput_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |