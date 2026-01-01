# RadioButtonGroupCommandInput.isVisible Property

Parent Object: [RadioButtonGroupCommandInput](RadioButtonGroupCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/RadioButtonGroupCommandInput.h>

## Description

Gets or sets if this input will be visible to the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"radioButtonGroupCommandInput\_var" is a variable referencing a RadioButtonGroupCommandInput object.  ```` ``` # Get the value of the property. propertyValue = radioButtonGroupCommandInput_var.isVisible  # Set the value of the property. radioButtonGroupCommandInput_var.isVisible = propertyValue ``` ```` |

"radioButtonGroupCommandInput\_var" is a variable referencing a RadioButtonGroupCommandInput object. ```` ``` #include <Core/UserInterface/RadioButtonGroupCommandInput.h>  // Get the value of the property. boolean propertyValue = radioButtonGroupCommandInput_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = radioButtonGroupCommandInput_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |