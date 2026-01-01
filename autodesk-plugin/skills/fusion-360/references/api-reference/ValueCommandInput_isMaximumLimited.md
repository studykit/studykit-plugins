# ValueCommandInput.isMaximumLimited Property

Parent Object: [ValueCommandInput](ValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ValueCommandInput.h>

## Description

Gets and sets whether the maximum value has a limit. The maximum limit is set using the maximumValue property, and the isMaximumInclusive property controls whether the maximum includes the maximum value or must be less than the maximum.

## Syntax

* [Python](#Python)
* [C++](#C++)

"valueCommandInput\_var" is a variable referencing a ValueCommandInput object.  ```` ``` # Get the value of the property. propertyValue = valueCommandInput_var.isMaximumLimited  # Set the value of the property. valueCommandInput_var.isMaximumLimited = propertyValue ``` ```` |

"valueCommandInput\_var" is a variable referencing a ValueCommandInput object. ```` ``` #include <Core/UserInterface/ValueCommandInput.h>  // Get the value of the property. boolean propertyValue = valueCommandInput_var->isMaximumLimited();  // Set the value of the property, where value_var is a boolean. bool returnValue = valueCommandInput_var->isMaximumLimited(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |