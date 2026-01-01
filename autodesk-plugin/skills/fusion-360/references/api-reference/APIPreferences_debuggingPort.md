# APIPreferences.debuggingPort Property

Parent Object: [APIPreferences](APIPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/APIPreferences.h>

## Description

Gets and sets the port used when connecting to Visual Studio Code.

## Syntax

* [Python](#Python)
* [C++](#C++)

"aPIPreferences\_var" is a variable referencing an APIPreferences object. |

"aPIPreferences\_var" is a variable referencing an APIPreferences object. ```` ``` #include <Core/Application/APIPreferences.h>  // Get the value of the property. integer propertyValue = aPIPreferences_var->debuggingPort();  // Set the value of the property, where value_var is an integer. bool returnValue = aPIPreferences_var->debuggingPort(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |