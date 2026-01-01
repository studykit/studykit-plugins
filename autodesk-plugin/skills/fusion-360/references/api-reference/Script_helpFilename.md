# Script.helpFilename Property

Parent Object: [Script](Script.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Script.h>

## Description

Returns the filename of a local html file that serves as the help file for this script or add-in. This filename is defined in the manifest of the script or add-in using the "helpFilename" setting.

## Syntax

* [Python](#Python)
* [C++](#C++)

"script\_var" is a variable referencing a Script object. |

"script\_var" is a variable referencing a Script object. ```` ``` #include <Core/Application/Script.h>  // Get the value of the property. string propertyValue = script_var->helpFilename(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |