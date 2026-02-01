# ValueCommandInput.maximumValue Property

Parent Object: [ValueCommandInput](ValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ValueCommandInput.h>

## Description

Gets and sets the maximum value for the input. Setting this value will automatically set the isMaximumLimited property to true, enabling the use of the maximum value. Use the isMaximumInclusive property to control if the maximum can be equal to this value or must be less than the maximum.

## Syntax

* [Python](#Python)
* [C++](#C++)

"valueCommandInput\_var" is a variable referencing a ValueCommandInput object. |

"valueCommandInput\_var" is a variable referencing a ValueCommandInput object. ```` ``` #include <Core/UserInterface/ValueCommandInput.h>  // Get the value of the property. double propertyValue = valueCommandInput_var->maximumValue();  // Set the value of the property, where value_var is a double. bool returnValue = valueCommandInput_var->maximumValue(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |