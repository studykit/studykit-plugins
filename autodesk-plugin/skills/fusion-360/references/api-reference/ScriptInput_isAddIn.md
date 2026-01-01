# ScriptInput.isAddIn Property

Parent Object: [ScriptInput](ScriptInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ScriptInput.h>

## Description

Specifies if a script or add-in is to be created. A value of true indicates an add-in will be created.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scriptInput\_var" is a variable referencing a ScriptInput object. |

"scriptInput\_var" is a variable referencing a ScriptInput object. ```` ``` #include <Core/Application/ScriptInput.h>  // Get the value of the property. boolean propertyValue = scriptInput_var->isAddIn();  // Set the value of the property, where value_var is a boolean. bool returnValue = scriptInput_var->isAddIn(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |