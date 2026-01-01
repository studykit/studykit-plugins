# CommandCreatedEventArgs.objectType Property

Parent Object: [CommandCreatedEventArgs](CommandCreatedEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandCreatedEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandCreatedEventArgs\_var" is a variable referencing a CommandCreatedEventArgs object.  ```` ``` # Get the value of the property. propertyValue = commandCreatedEventArgs_var.objectType ``` ```` |

"commandCreatedEventArgs\_var" is a variable referencing a CommandCreatedEventArgs object. ```` ``` #include <Core/UserInterface/CommandCreatedEventArgs.h>  // Get the value of the property. string propertyValue = commandCreatedEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |