# KeyboardEvent.objectType Property

Parent Object: [KeyboardEvent](KeyboardEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/KeyboardEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"keyboardEvent\_var" is a variable referencing a KeyboardEvent object.  ```` ``` # Get the value of the property. propertyValue = keyboardEvent_var.objectType ``` ```` |

"keyboardEvent\_var" is a variable referencing a KeyboardEvent object. ```` ``` #include <Core/UserInterface/KeyboardEvent.h>  // Get the value of the property. string propertyValue = keyboardEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |