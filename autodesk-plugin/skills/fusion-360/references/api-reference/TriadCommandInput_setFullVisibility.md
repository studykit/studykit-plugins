# TriadCommandInput.setFullVisibility Method

Parent Object: [TriadCommandInput](TriadCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TriadCommandInput.h>

## Description

A convenience method to turn on and off the visibility of commonly used controls in a triad. These include the X, Y, and Z axis translations, the X, Y, and Z axis rotations, scaling in the X, Y, and Z directions, scaling on the X-Y, Y-Z and Z-X planes, translation on the X-Y, Y-Z, and Z-X planes, and the origin move.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triadCommandInput\_var" is a variable referencing a [TriadCommandInput](TriadCommandInput.htm) object.```` ``` returnValue = triadCommandInput_var.setFullVisibility(isVisible) ``` ```` |

"triadCommandInput\_var" is a variable referencing a [TriadCommandInput](TriadCommandInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if it was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| isVisible | boolean | Defines if the visibility of the controls should be turned on or off. True indicates they will be visible. |

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |