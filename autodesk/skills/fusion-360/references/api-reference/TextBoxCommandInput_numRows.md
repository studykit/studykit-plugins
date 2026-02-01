# TextBoxCommandInput.numRows Property

Parent Object: [TextBoxCommandInput](TextBoxCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextBoxCommandInput.h>

## Description

Gets and sets the height of the text box as defined by the number of rows of text that can be displayed. If the text is larger than will fit in the box a scroll bar will automatically be displayed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textBoxCommandInput\_var" is a variable referencing a TextBoxCommandInput object. |

"textBoxCommandInput\_var" is a variable referencing a TextBoxCommandInput object. ```` ``` #include <Core/UserInterface/TextBoxCommandInput.h>  // Get the value of the property. integer propertyValue = textBoxCommandInput_var->numRows();  // Set the value of the property, where value_var is an integer. bool returnValue = textBoxCommandInput_var->numRows(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |