# ScriptInput.programmingLanguage Property

Parent Object: [ScriptInput](ScriptInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ScriptInput.h>

## Description

Gets and sets which programming language the new script or add-in will use.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scriptInput\_var" is a variable referencing a ScriptInput object. |

"scriptInput\_var" is a variable referencing a ScriptInput object. ```` ``` #include <Core/Application/ScriptInput.h>  // Get the value of the property. ProgrammingLanguages propertyValue = scriptInput_var->programmingLanguage();  // Set the value of the property, where value_var is a ProgrammingLanguages. bool returnValue = scriptInput_var->programmingLanguage(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ProgrammingLanguages](ProgrammingLanguages.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |