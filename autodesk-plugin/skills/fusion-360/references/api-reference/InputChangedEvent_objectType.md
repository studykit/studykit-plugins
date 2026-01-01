# InputChangedEvent.objectType Property

Parent Object: [InputChangedEvent](InputChangedEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/InputChangedEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"inputChangedEvent\_var" is a variable referencing an InputChangedEvent object.  ```` ``` # Get the value of the property. propertyValue = inputChangedEvent_var.objectType ``` ```` |

"inputChangedEvent\_var" is a variable referencing an InputChangedEvent object. ```` ``` #include <Core/UserInterface/InputChangedEvent.h>  // Get the value of the property. string propertyValue = inputChangedEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |