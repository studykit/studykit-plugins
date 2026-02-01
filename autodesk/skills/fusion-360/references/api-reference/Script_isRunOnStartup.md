# Script.isRunOnStartup Property

Parent Object: [Script](Script.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Script.h>

## Description

Gets and sets whether this add-in will automatically run when Fusion is started. This property is only valid when the isAddIn property returns true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"script\_var" is a variable referencing a Script object. |

"script\_var" is a variable referencing a Script object. ```` ``` #include <Core/Application/Script.h>  // Get the value of the property. boolean propertyValue = script_var->isRunOnStartup();  // Set the value of the property, where value_var is a boolean. bool returnValue = script_var->isRunOnStartup(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |