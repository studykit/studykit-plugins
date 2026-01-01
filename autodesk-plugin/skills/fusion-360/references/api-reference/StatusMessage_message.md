# StatusMessage.message Property

Parent Object: [StatusMessage](StatusMessage.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/StatusMessage.h>

## Description

The user visible message being used. Setting this message for custom feature errors or warnings is currently ignored.

## Syntax

* [Python](#Python)
* [C++](#C++)

"statusMessage\_var" is a variable referencing a StatusMessage object. |

"statusMessage\_var" is a variable referencing a StatusMessage object. ```` ``` #include <Core/Application/StatusMessage.h>  // Get the value of the property. string propertyValue = statusMessage_var->message();  // Set the value of the property, where value_var is a string. bool returnValue = statusMessage_var->message(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |