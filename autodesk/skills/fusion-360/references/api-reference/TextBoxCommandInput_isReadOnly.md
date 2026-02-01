# TextBoxCommandInput.isReadOnly Property

Parent Object: [TextBoxCommandInput](TextBoxCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextBoxCommandInput.h>

## Description

Gets and sets if the text box is read-only or not. If it is read-only the user cannot edit the text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textBoxCommandInput\_var" is a variable referencing a TextBoxCommandInput object. |

"textBoxCommandInput\_var" is a variable referencing a TextBoxCommandInput object. ```` ``` #include <Core/UserInterface/TextBoxCommandInput.h>  // Get the value of the property. boolean propertyValue = textBoxCommandInput_var->isReadOnly();  // Set the value of the property, where value_var is a boolean. bool returnValue = textBoxCommandInput_var->isReadOnly(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |