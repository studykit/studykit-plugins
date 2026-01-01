# TriadCommandInput.setScaleVisibility Method

Parent Object: [TriadCommandInput](TriadCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TriadCommandInput.h>

## Description

A convenience method to turn on and off the visibility of the controls that define scaling in the X, Y, and Z direction and the X-Y, Y-Z, and Z-X planes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"triadCommandInput\_var" is a variable referencing a [TriadCommandInput](TriadCommandInput.htm) object.```` ``` returnValue = triadCommandInput_var.setScaleVisibility(isVisible) ``` ```` |

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