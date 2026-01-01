# TriadCommandInput.zXPlaneScaleFactorExpression Property

Parent Object: [TriadCommandInput](TriadCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TriadCommandInput.h>

## Description

Gets or sets the expression displayed in the input field for the Z-X plane scale. This can contain equations and references to parameters but must result in a valid unitless expression.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object. |

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object. ```` ``` #include <Core/UserInterface/TriadCommandInput.h>  // Get the value of the property. string propertyValue = triadCommandInput_var->zXPlaneScaleFactorExpression();  // Set the value of the property, where value_var is a string. bool returnValue = triadCommandInput_var->zXPlaneScaleFactorExpression(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |