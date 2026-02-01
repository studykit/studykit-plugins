# DataEvent.sender Property

Parent Object: [DataEvent](DataEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataEvent\_var" is a variable referencing a DataEvent object. |

"dataEvent\_var" is a variable referencing a DataEvent object. ```` ``` #include <Core/Dashboard/DataEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = dataEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |