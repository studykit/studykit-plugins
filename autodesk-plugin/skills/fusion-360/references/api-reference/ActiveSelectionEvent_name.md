# ActiveSelectionEvent.name Property

Parent Object: [ActiveSelectionEvent](ActiveSelectionEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ActiveSelectionEvent.h>

## Description

The name of the event - e.g. "DocumentOpening"

## Syntax

* [Python](#Python)
* [C++](#C++)

"activeSelectionEvent\_var" is a variable referencing an ActiveSelectionEvent object. |

"activeSelectionEvent\_var" is a variable referencing an ActiveSelectionEvent object. ```` ``` #include <Core/UserInterface/ActiveSelectionEvent.h>  // Get the value of the property. string propertyValue = activeSelectionEvent_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |