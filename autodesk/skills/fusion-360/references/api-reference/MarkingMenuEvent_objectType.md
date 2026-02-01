# MarkingMenuEvent.objectType Property

Parent Object: [MarkingMenuEvent](MarkingMenuEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MarkingMenuEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"markingMenuEvent\_var" is a variable referencing a MarkingMenuEvent object.  ```` ``` # Get the value of the property. propertyValue = markingMenuEvent_var.objectType ``` ```` |

"markingMenuEvent\_var" is a variable referencing a MarkingMenuEvent object. ```` ``` #include <Core/UserInterface/MarkingMenuEvent.h>  // Get the value of the property. string propertyValue = markingMenuEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |