# Command.cancelButtonText Property

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Gets and sets the text displayed on the Cancel button. The value of this property is ignored if the isCancelButtonVisible property is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"command\_var" is a variable referencing a Command object. |

"command\_var" is a variable referencing a Command object. ```` ``` #include <Core/UserInterface/Command.h>  // Get the value of the property. string propertyValue = command_var->cancelButtonText();  // Set the value of the property, where value_var is a string. bool returnValue = command_var->cancelButtonText(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |