# TriadCommandInput.isVisible Property

Parent Object: [TriadCommandInput](TriadCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TriadCommandInput.h>

## Description

Gets or sets if this input will be visible to the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object.  ```` ``` # Get the value of the property. propertyValue = triadCommandInput_var.isVisible  # Set the value of the property. triadCommandInput_var.isVisible = propertyValue ``` ```` |

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object. ```` ``` #include <Core/UserInterface/TriadCommandInput.h>  // Get the value of the property. boolean propertyValue = triadCommandInput_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = triadCommandInput_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |