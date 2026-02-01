# TriadCommandInput.zXPlaneScaleFactor Property

Parent Object: [TriadCommandInput](TriadCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TriadCommandInput.h>

## Description

Gets and sets the current value of the scale factor on the Z-X plane of the triad.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object.  ```` ``` # Get the value of the property. propertyValue = triadCommandInput_var.zXPlaneScaleFactor  # Set the value of the property. triadCommandInput_var.zXPlaneScaleFactor = propertyValue ``` ```` |

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object. ```` ``` #include <Core/UserInterface/TriadCommandInput.h>  // Get the value of the property. double propertyValue = triadCommandInput_var->zXPlaneScaleFactor();  // Set the value of the property, where value_var is a double. bool returnValue = triadCommandInput_var->zXPlaneScaleFactor(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |