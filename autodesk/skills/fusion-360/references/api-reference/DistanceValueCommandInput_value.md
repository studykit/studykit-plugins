# DistanceValueCommandInput.value Property

Parent Object: [DistanceValueCommandInput](DistanceValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DistanceValueCommandInput.h>

## Description

Gets and sets the current value of the command input. The value is in centimeters but will be displayed to the user in the current default document units. Setting this value can fail if the input value is not within the minimum and maximum value range.

## Syntax

* [Python](#Python)
* [C++](#C++)

"distanceValueCommandInput\_var" is a variable referencing a DistanceValueCommandInput object.  ```` ``` # Get the value of the property. propertyValue = distanceValueCommandInput_var.value  # Set the value of the property. distanceValueCommandInput_var.value = propertyValue ``` ```` |

"distanceValueCommandInput\_var" is a variable referencing a DistanceValueCommandInput object. ```` ``` #include <Core/UserInterface/DistanceValueCommandInput.h>  // Get the value of the property. double propertyValue = distanceValueCommandInput_var->value();  // Set the value of the property, where value_var is a double. bool returnValue = distanceValueCommandInput_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |