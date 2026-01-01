# CommandEvent.objectType Property

Parent Object: [CommandEvent](CommandEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandEvent\_var" is a variable referencing a CommandEvent object.  ```` ``` # Get the value of the property. propertyValue = commandEvent_var.objectType ``` ```` |

"commandEvent\_var" is a variable referencing a CommandEvent object. ```` ``` #include <Core/UserInterface/CommandEvent.h>  // Get the value of the property. string propertyValue = commandEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |