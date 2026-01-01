# Script.id Property

Parent Object: [Script](Script.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Script.h>

## Description

Gets the ID of this script or add-in. This is typically a GUID and is assumed to be unique with respect to all other add-ins.

## Syntax

* [Python](#Python)
* [C++](#C++)

"script\_var" is a variable referencing a Script object. |

"script\_var" is a variable referencing a Script object. ```` ``` #include <Core/Application/Script.h>  // Get the value of the property. string propertyValue = script_var->id(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |