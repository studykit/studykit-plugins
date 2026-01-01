# Script.isVisible Property

Parent Object: [Script](Script.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Script.h>

## Description

Gets and sets whether the script or add-in is visible within the “Scripts and Add-Ins” dialog. By default, all scripts and add-ins are visible. Setting this to false will cause it to be hidden and unloaded if it is already running. Also, if it’s an add-in set to load on startup, it will no longer be loaded.

## Syntax

* [Python](#Python)
* [C++](#C++)

"script\_var" is a variable referencing a Script object. |

"script\_var" is a variable referencing a Script object. ```` ``` #include <Core/Application/Script.h>  // Get the value of the property. boolean propertyValue = script_var->isVisible();  // Set the value of the property, where value_var is a boolean. bool returnValue = script_var->isVisible(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |