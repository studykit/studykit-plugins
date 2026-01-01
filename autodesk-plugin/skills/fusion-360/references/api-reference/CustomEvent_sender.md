# CustomEvent.sender Property

Parent Object: [CustomEvent](CustomEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CustomEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customEvent\_var" is a variable referencing a CustomEvent object. |

"customEvent\_var" is a variable referencing a CustomEvent object. ```` ``` #include <Core/Application/CustomEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = customEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |