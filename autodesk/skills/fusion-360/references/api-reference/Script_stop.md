# Script.stop Method

Parent Object: [Script](Script.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Script.h>

## Description

If this script or add-in is running, this method will stop it. The isRunning property can be used to determine if it is running. If the script or add-in is not running and this method is called, there is no effect.

## Syntax

* [Python](#Python)
* [C++](#C++)

"script\_var" is a variable referencing a [Script](Script.htm) object.```` ``` returnValue = script_var.stop() ``` ```` |

"script\_var" is a variable referencing a [Script](Script.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |