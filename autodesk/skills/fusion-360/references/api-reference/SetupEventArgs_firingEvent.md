# SetupEventArgs.firingEvent Property

Parent Object: [SetupEventArgs](SetupEventArgs.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupEventArgs\_var" is a variable referencing a SetupEventArgs object. |

"setupEventArgs\_var" is a variable referencing a SetupEventArgs object. ```` ``` #include <Cam/CAM/SetupEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = setupEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |