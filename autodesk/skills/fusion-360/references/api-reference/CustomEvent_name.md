# CustomEvent.name Property

Parent Object: [CustomEvent](CustomEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CustomEvent.h>

## Description

The name of the event - e.g. "DocumentOpening"

## Syntax

* [Python](#Python)
* [C++](#C++)

"customEvent\_var" is a variable referencing a CustomEvent object. |

"customEvent\_var" is a variable referencing a CustomEvent object. ```` ``` #include <Core/Application/CustomEvent.h>  // Get the value of the property. string propertyValue = customEvent_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |