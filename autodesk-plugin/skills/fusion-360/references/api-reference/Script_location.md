# Script.location Property

Parent Object: [Script](Script.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Script.h>

## Description

Gets which standard location this script is located.

## Syntax

* [Python](#Python)
* [C++](#C++)

"script\_var" is a variable referencing a Script object. |

"script\_var" is a variable referencing a Script object. ```` ``` #include <Core/Application/Script.h>  // Get the value of the property. ScriptSourceLocations propertyValue = script_var->location(); ``` ```` |

## Property Value

This is a read only property whose value is a [ScriptSourceLocations](ScriptSourceLocations.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |