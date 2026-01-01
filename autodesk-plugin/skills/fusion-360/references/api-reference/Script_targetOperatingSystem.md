# Script.targetOperatingSystem Property

Parent Object: [Script](Script.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Script.h>

## Description

Returns the operating systems this script or add-in is available for.

## Syntax

* [Python](#Python)
* [C++](#C++)

"script\_var" is a variable referencing a Script object. |

"script\_var" is a variable referencing a Script object. ```` ``` #include <Core/Application/Script.h>  // Get the value of the property. OperatingSystems propertyValue = script_var->targetOperatingSystem(); ``` ```` |

## Property Value

This is a read only property whose value is an [OperatingSystems](OperatingSystems.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |