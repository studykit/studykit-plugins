# CommandCreatedEvent.objectType Property

Parent Object: [CommandCreatedEvent](CommandCreatedEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandCreatedEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandCreatedEvent\_var" is a variable referencing a CommandCreatedEvent object.  ```` ``` # Get the value of the property. propertyValue = commandCreatedEvent_var.objectType ``` ```` |

"commandCreatedEvent\_var" is a variable referencing a CommandCreatedEvent object. ```` ``` #include <Core/UserInterface/CommandCreatedEvent.h>  // Get the value of the property. string propertyValue = commandCreatedEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |