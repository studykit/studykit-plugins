# AngleValueCommandInput.expression Property

Parent Object: [AngleValueCommandInput](AngleValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/AngleValueCommandInput.h>

## Description

Gets or sets the expression displayed in the input field. This can contain equations and references to parameters but must result in a valid angle expression. If units are not specified as part of the expression, the default user units of degrees are used.

## Syntax

* [Python](#Python)
* [C++](#C++)

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object. |

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object. ```` ``` #include <Core/UserInterface/AngleValueCommandInput.h>  // Get the value of the property. string propertyValue = angleValueCommandInput_var->expression();  // Set the value of the property, where value_var is a string. bool returnValue = angleValueCommandInput_var->expression(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |