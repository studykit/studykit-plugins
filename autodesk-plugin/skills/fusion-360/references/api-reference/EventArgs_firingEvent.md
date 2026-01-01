# EventArgs.firingEvent Property

Parent Object: [EventArgs](EventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/EventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"eventArgs\_var" is a variable referencing an EventArgs object. |

"eventArgs\_var" is a variable referencing an EventArgs object. ```` ``` #include <Core/Application/EventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = eventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |