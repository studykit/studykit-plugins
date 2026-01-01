# HttpEvent.name Property

Parent Object: [HttpEvent](HttpEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpEvent.h>

## Description

The name of the event - e.g. "DocumentOpening"

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpEvent\_var" is a variable referencing a HttpEvent object. |

"httpEvent\_var" is a variable referencing a HttpEvent object. ```` ``` #include <Core/Application/HttpEvent.h>  // Get the value of the property. string propertyValue = httpEvent_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |