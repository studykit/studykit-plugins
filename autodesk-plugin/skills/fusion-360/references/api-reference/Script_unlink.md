# Script.unlink Method

Parent Object: [Script](Script.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Script.h>

## Description

Unlinks this script or add-in. This removes it from Fusion's list of linked scripts and add-ins, so it is no longer displayed in the dialog, and if it's an add-in, it will no longer run on startup.

## Syntax

* [Python](#Python)
* [C++](#C++)

"script\_var" is a variable referencing a [Script](Script.htm) object.```` ``` returnValue = script_var.unlink() ``` ```` |

"script\_var" is a variable referencing a [Script](Script.htm) object.  ```` ``` #include <Core/Application/Script.h>  returnValue = script_var->unlink(); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the unlink was successful. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |