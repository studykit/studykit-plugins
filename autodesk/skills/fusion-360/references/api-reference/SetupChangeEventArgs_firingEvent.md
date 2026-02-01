# SetupChangeEventArgs.firingEvent Property

Parent Object: [SetupChangeEventArgs](SetupChangeEventArgs.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupChangeEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupChangeEventArgs\_var" is a variable referencing a SetupChangeEventArgs object. |

"setupChangeEventArgs\_var" is a variable referencing a SetupChangeEventArgs object. ```` ``` #include <Cam/CAM/SetupChangeEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = setupChangeEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |