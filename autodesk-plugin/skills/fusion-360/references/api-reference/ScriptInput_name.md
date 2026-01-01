# ScriptInput.name Property

Parent Object: [ScriptInput](ScriptInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ScriptInput.h>

## Description

Gets and sets the name of the script or add-in to create. This name must be unique with respect to the other scripts and add-ins in the folder specified by the targetFolder property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scriptInput\_var" is a variable referencing a ScriptInput object. |

"scriptInput\_var" is a variable referencing a ScriptInput object. ```` ``` #include <Core/Application/ScriptInput.h>  // Get the value of the property. string propertyValue = scriptInput_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = scriptInput_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |