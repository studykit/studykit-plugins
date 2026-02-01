# ScriptInput.targetFolder Property

Parent Object: [ScriptInput](ScriptInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ScriptInput.h>

## Description

The full path to the folder where the script or add-in will be created. By default, this is an empty string which uses the default folder specified by the "Default Path for Scripts and Add-Ins" preference. Specifying a path overrides the default and will create the script or add-in in the specified location. No "Scripts" or "AddIns" sub-folder is created.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scriptInput\_var" is a variable referencing a ScriptInput object. |

"scriptInput\_var" is a variable referencing a ScriptInput object. ```` ``` #include <Core/Application/ScriptInput.h>  // Get the value of the property. string propertyValue = scriptInput_var->targetFolder();  // Set the value of the property, where value_var is a string. bool returnValue = scriptInput_var->targetFolder(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |