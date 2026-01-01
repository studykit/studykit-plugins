# ScriptInput.runOnStartup Property

Parent Object: [ScriptInput](ScriptInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ScriptInput.h>

## Description

If this Script represents an add-in and isAddIn is True, this specifies if the add-in should be automatically started when Fusion starts up.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scriptInput\_var" is a variable referencing a ScriptInput object. |

"scriptInput\_var" is a variable referencing a ScriptInput object. ```` ``` #include <Core/Application/ScriptInput.h>  // Get the value of the property. boolean propertyValue = scriptInput_var->runOnStartup();  // Set the value of the property, where value_var is a boolean. bool returnValue = scriptInput_var->runOnStartup(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |