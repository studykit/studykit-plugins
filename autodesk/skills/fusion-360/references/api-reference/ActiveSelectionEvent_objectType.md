# ActiveSelectionEvent.objectType Property

Parent Object: [ActiveSelectionEvent](ActiveSelectionEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ActiveSelectionEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"activeSelectionEvent\_var" is a variable referencing an ActiveSelectionEvent object.  ```` ``` # Get the value of the property. propertyValue = activeSelectionEvent_var.objectType ``` ```` |

"activeSelectionEvent\_var" is a variable referencing an ActiveSelectionEvent object. ```` ``` #include <Core/UserInterface/ActiveSelectionEvent.h>  // Get the value of the property. string propertyValue = activeSelectionEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |