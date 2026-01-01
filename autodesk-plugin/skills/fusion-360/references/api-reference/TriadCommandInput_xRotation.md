# TriadCommandInput.xRotation Property

Parent Object: [TriadCommandInput](TriadCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TriadCommandInput.h>

## Description

Gets and sets the current value of the rotation around the X axis of the triad. The value is in radians but will be displayed to the user in degrees.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object.  ```` ``` # Get the value of the property. propertyValue = triadCommandInput_var.xRotation  # Set the value of the property. triadCommandInput_var.xRotation = propertyValue ``` ```` |

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object. ```` ``` #include <Core/UserInterface/TriadCommandInput.h>  // Get the value of the property. double propertyValue = triadCommandInput_var->xRotation();  // Set the value of the property, where value_var is a double. bool returnValue = triadCommandInput_var->xRotation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |