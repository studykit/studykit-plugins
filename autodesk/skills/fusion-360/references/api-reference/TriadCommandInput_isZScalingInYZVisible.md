# TriadCommandInput.isZScalingInYZVisible Property

Parent Object: [TriadCommandInput](TriadCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TriadCommandInput.h>

## Description

Gets and sets if the control that defines the scaling along the Z axis is visible in both the graphical manipulator and in the dialog. This control lies on the Y-Z plane of the triad.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object. |

"triadCommandInput\_var" is a variable referencing a TriadCommandInput object. ```` ``` #include <Core/UserInterface/TriadCommandInput.h>  // Get the value of the property. boolean propertyValue = triadCommandInput_var->isZScalingInYZVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = triadCommandInput_var->isZScalingInYZVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |