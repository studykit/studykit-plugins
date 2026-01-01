# Script.programmingLanguage Property

Parent Object: [Script](Script.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Script.h>

## Description

Returns the programming language this script or add-in is written in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"script\_var" is a variable referencing a Script object. |

"script\_var" is a variable referencing a Script object. ```` ``` #include <Core/Application/Script.h>  // Get the value of the property. ProgrammingLanguages propertyValue = script_var->programmingLanguage(); ``` ```` |

## Property Value

This is a read only property whose value is a [ProgrammingLanguages](ProgrammingLanguages.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |