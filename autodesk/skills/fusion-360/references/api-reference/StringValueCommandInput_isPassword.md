# StringValueCommandInput.isPassword Property

Parent Object: [StringValueCommandInput](StringValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/StringValueCommandInput.h>

## Description

Gets or sets if this string input behaves as a password field. This defaults to false for a newly created StringValueCommandInput. If true, dots are displayed instead of the actual characters but the value property will get and set the actual string.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stringValueCommandInput\_var" is a variable referencing a StringValueCommandInput object. |

"stringValueCommandInput\_var" is a variable referencing a StringValueCommandInput object. ```` ``` #include <Core/UserInterface/StringValueCommandInput.h>  // Get the value of the property. boolean propertyValue = stringValueCommandInput_var->isPassword();  // Set the value of the property, where value_var is a boolean. bool returnValue = stringValueCommandInput_var->isPassword(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |