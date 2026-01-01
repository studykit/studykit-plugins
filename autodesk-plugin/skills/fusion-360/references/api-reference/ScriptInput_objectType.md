# ScriptInput.objectType Property

Parent Object: [ScriptInput](ScriptInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ScriptInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scriptInput\_var" is a variable referencing a ScriptInput object.  ```` ``` # Get the value of the property. propertyValue = scriptInput_var.objectType ``` ```` |

"scriptInput\_var" is a variable referencing a ScriptInput object. ```` ``` #include <Core/Application/ScriptInput.h>  // Get the value of the property. string propertyValue = scriptInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |