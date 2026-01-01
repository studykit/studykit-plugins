# InputChangedEvent.name Property

Parent Object: [InputChangedEvent](InputChangedEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/InputChangedEvent.h>

## Description

The name of the event - e.g. "DocumentOpening"

## Syntax

* [Python](#Python)
* [C++](#C++)

"inputChangedEvent\_var" is a variable referencing an InputChangedEvent object. |

"inputChangedEvent\_var" is a variable referencing an InputChangedEvent object. ```` ``` #include <Core/UserInterface/InputChangedEvent.h>  // Get the value of the property. string propertyValue = inputChangedEvent_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |