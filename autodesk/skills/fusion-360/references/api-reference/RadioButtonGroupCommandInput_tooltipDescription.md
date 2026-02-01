# RadioButtonGroupCommandInput.tooltipDescription Property

Parent Object: [RadioButtonGroupCommandInput](RadioButtonGroupCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/RadioButtonGroupCommandInput.h>

## Description

Gets or sets additional text to display progressively along with the tooltip. The text for the description can contain some basic HTML formatting tags to format the tags. For example the br tag can be used to create multiple paragraphs. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"radioButtonGroupCommandInput\_var" is a variable referencing a RadioButtonGroupCommandInput object. |

"radioButtonGroupCommandInput\_var" is a variable referencing a RadioButtonGroupCommandInput object. ```` ``` #include <Core/UserInterface/RadioButtonGroupCommandInput.h>  // Get the value of the property. string propertyValue = radioButtonGroupCommandInput_var->tooltipDescription();  // Set the value of the property, where value_var is a string. bool returnValue = radioButtonGroupCommandInput_var->tooltipDescription(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |