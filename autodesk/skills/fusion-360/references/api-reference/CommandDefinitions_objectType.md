# CommandDefinitions.objectType Property

Parent Object: [CommandDefinitions](CommandDefinitions.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandDefinitions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandDefinitions\_var" is a variable referencing a CommandDefinitions object.  ```` ``` # Get the value of the property. propertyValue = commandDefinitions_var.objectType ``` ```` |

"commandDefinitions\_var" is a variable referencing a CommandDefinitions object. ```` ``` #include <Core/UserInterface/CommandDefinitions.h>  // Get the value of the property. string propertyValue = commandDefinitions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |