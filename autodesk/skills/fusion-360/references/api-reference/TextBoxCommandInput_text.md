# TextBoxCommandInput.text Property

Parent Object: [TextBoxCommandInput](TextBoxCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextBoxCommandInput.h>

## Description

Gets and sets the text in the text box. When text is set using the text property, any HTML formatting is ignored and the full string will be displayed in the text box. For example, if you specify the string "Here is a <b>Bold</b> word", and use the formattedText property, you will see "Here is a **Bold** word" in the text box. However, if you use the text property, you will see "Here is a <b>Bold</b> word" and when you get the text property you will get back "Here is a <b>Bold</b> word". This can be useful if you're using the text box to have the user enter HTML code so it's treated as a simple string.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textBoxCommandInput\_var" is a variable referencing a TextBoxCommandInput object. |

"textBoxCommandInput\_var" is a variable referencing a TextBoxCommandInput object. ```` ``` #include <Core/UserInterface/TextBoxCommandInput.h>  // Get the value of the property. string propertyValue = textBoxCommandInput_var->text();  // Set the value of the property, where value_var is a string. bool returnValue = textBoxCommandInput_var->text(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |