# AngleValueCommandInput.value Property

Parent Object: [AngleValueCommandInput](AngleValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/AngleValueCommandInput.h>

## Description

Gets and sets the current value of the command input. The value is in radians but will be displayed to the user in degrees. Setting this value can fail if the input value is not within the minimum and maximum value range.

## Syntax

* [Python](#Python)
* [C++](#C++)

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object.  ```` ``` # Get the value of the property. propertyValue = angleValueCommandInput_var.value  # Set the value of the property. angleValueCommandInput_var.value = propertyValue ``` ```` |

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object. ```` ``` #include <Core/UserInterface/AngleValueCommandInput.h>  // Get the value of the property. double propertyValue = angleValueCommandInput_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = angleValueCommandInput_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |