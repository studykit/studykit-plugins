# ScriptInput.targetOperatingSystem Property

Parent Object: [ScriptInput](ScriptInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ScriptInput.h>

## Description

Specifies the operating systems this script or add-in will be displayed in the "Scripts and Add-Ins" dialog and where it will be automatically run on startup, if that option is specified. Defaults to WindowsAndMacOperatingSystem

## Syntax

* [Python](#Python)
* [C++](#C++)

"scriptInput\_var" is a variable referencing a ScriptInput object. |

"scriptInput\_var" is a variable referencing a ScriptInput object. ```` ``` #include <Core/Application/ScriptInput.h>  // Get the value of the property. OperatingSystems propertyValue = scriptInput_var->targetOperatingSystem();  // Set the value of the property, where value_var is an OperatingSystems. bool returnValue = scriptInput_var->targetOperatingSystem(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [OperatingSystems](OperatingSystems.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |