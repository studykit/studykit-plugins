# WebRequestEvent.sender Property

Parent Object: [WebRequestEvent](WebRequestEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/WebRequestEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webRequestEvent\_var" is a variable referencing a WebRequestEvent object. |

"webRequestEvent\_var" is a variable referencing a WebRequestEvent object. ```` ``` #include <Core/Application/WebRequestEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = webRequestEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |