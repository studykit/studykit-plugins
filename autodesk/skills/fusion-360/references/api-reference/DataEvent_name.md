# DataEvent.name Property

Parent Object: [DataEvent](DataEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataEvent.h>

## Description

The name of the event - e.g. "DocumentOpening"

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataEvent\_var" is a variable referencing a DataEvent object. |

"dataEvent\_var" is a variable referencing a DataEvent object. ```` ``` #include <Core/Dashboard/DataEvent.h>  // Get the value of the property. string propertyValue = dataEvent_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |