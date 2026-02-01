# HttpEvent.sender Property

Parent Object: [HttpEvent](HttpEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpEvent\_var" is a variable referencing a HttpEvent object. |

"httpEvent\_var" is a variable referencing a HttpEvent object. ```` ``` #include <Core/Application/HttpEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = httpEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |