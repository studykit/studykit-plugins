# ApplicationEvent.sender Property

Parent Object: [ApplicationEvent](ApplicationEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ApplicationEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationEvent\_var" is a variable referencing an ApplicationEvent object. |

"applicationEvent\_var" is a variable referencing an ApplicationEvent object. ```` ``` #include <Core/Application/ApplicationEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = applicationEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |