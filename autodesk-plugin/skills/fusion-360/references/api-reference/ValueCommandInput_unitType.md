# ValueCommandInput.unitType Property

Parent Object: [ValueCommandInput](ValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ValueCommandInput.h>

## Description

Gets and sets the unit type that is used when evaluating the user's input.

## Syntax

* [Python](#Python)
* [C++](#C++)

"valueCommandInput\_var" is a variable referencing a ValueCommandInput object. |

"valueCommandInput\_var" is a variable referencing a ValueCommandInput object. ```` ``` #include <Core/UserInterface/ValueCommandInput.h>  // Get the value of the property. string propertyValue = valueCommandInput_var->unitType();  // Set the value of the property, where value_var is a string. bool returnValue = valueCommandInput_var->unitType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |