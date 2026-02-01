# ApplicationCommandEvent.objectType Property

Parent Object: [ApplicationCommandEvent](ApplicationCommandEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ApplicationCommandEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationCommandEvent\_var" is a variable referencing an ApplicationCommandEvent object.  ```` ``` # Get the value of the property. propertyValue = applicationCommandEvent_var.objectType ``` ```` |

"applicationCommandEvent\_var" is a variable referencing an ApplicationCommandEvent object. ```` ``` #include <Core/UserInterface/ApplicationCommandEvent.h>  // Get the value of the property. string propertyValue = applicationCommandEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |