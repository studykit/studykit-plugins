# TextBoxCommandInput.isVisible Property

Parent Object: [TextBoxCommandInput](TextBoxCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextBoxCommandInput.h>

## Description

Gets or sets if this input will be visible to the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textBoxCommandInput\_var" is a variable referencing a TextBoxCommandInput object.  ```` ``` # Get the value of the property. propertyValue = textBoxCommandInput_var.isVisible  # Set the value of the property. textBoxCommandInput_var.isVisible = propertyValue ``` ```` |

"textBoxCommandInput\_var" is a variable referencing a TextBoxCommandInput object. ```` ``` #include <Core/UserInterface/TextBoxCommandInput.h>  // Get the value of the property. boolean propertyValue = textBoxCommandInput_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = textBoxCommandInput_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |