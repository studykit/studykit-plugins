# SetupEvent.sender Property

Parent Object: [SetupEvent](SetupEvent.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupEvent\_var" is a variable referencing a SetupEvent object. |

"setupEvent\_var" is a variable referencing a SetupEvent object. ```` ``` #include <Cam/CAM/SetupEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = setupEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |