# BoolValueCommandInput.value Property

Parent Object: [BoolValueCommandInput](BoolValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/BoolValueCommandInput.h>

## Description

Gets or sets the state of this input. If it's being displayed as a check box a value of true indicates the input is checked. If it's being displayed as a button, a value of true indicates the button is currently depressed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boolValueCommandInput\_var" is a variable referencing a BoolValueCommandInput object. |

"boolValueCommandInput\_var" is a variable referencing a BoolValueCommandInput object. ```` ``` #include <Core/UserInterface/BoolValueCommandInput.h>  // Get the value of the property. boolean propertyValue = boolValueCommandInput_var->value();  // Set the value of the property, where value_var is a boolean. bool returnValue = boolValueCommandInput_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |