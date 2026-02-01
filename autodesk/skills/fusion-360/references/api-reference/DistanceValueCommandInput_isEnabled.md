# DistanceValueCommandInput.isEnabled Property

Parent Object: [DistanceValueCommandInput](DistanceValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/DistanceValueCommandInput.h>

## Description

Gets or sets if this input is currently enabled or disabled for user interaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"distanceValueCommandInput\_var" is a variable referencing a DistanceValueCommandInput object.  ```` ``` # Get the value of the property. propertyValue = distanceValueCommandInput_var.isEnabled  # Set the value of the property. distanceValueCommandInput_var.isEnabled = propertyValue ``` ```` |

"distanceValueCommandInput\_var" is a variable referencing a DistanceValueCommandInput object. ```` ``` #include <Core/UserInterface/DistanceValueCommandInput.h>  // Get the value of the property. boolean propertyValue = distanceValueCommandInput_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = distanceValueCommandInput_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |