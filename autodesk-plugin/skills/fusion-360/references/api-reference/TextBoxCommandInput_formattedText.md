# TextBoxCommandInput.formattedText Property

Parent Object: [TextBoxCommandInput](TextBoxCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextBoxCommandInput.h>

## Description

Gets and sets the formatted text displayed in the dialog.

## Remarks

Formatted text includes any basic HTML formatting that has been defined. For example, you can use basic HTML formatting such as `<b>Bold</b>`, `<i>Italic</i>`, and `<br />` for a line break. It also supports hyper-links, which when clicked by the user, Fusion will open the specified URL in the default browser. Hyper-links are defined using the `<a>` tag such as "`You are using Autodesk's <a href=http://fusion.autodesk.com>Fusion</a>.`".
When setting the formattedText it's assumed the string has HTML formatting and it's best if the TextBoxCommandInput is set the input to be read-only. If the user edits formatted text, the result that's returned by both the formattedText and the text property may not always be as expected. If you want the user to enter or edit text in the text input, then you use the text property to define the text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textBoxCommandInput\_var" is a variable referencing a TextBoxCommandInput object. |

"textBoxCommandInput\_var" is a variable referencing a TextBoxCommandInput object. ```` ``` #include <Core/UserInterface/TextBoxCommandInput.h>  // Get the value of the property. string propertyValue = textBoxCommandInput_var->formattedText();  // Set the value of the property, where value_var is a string. bool returnValue = textBoxCommandInput_var->formattedText(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |