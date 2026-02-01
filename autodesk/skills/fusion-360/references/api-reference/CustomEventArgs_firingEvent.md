# CustomEventArgs.firingEvent Property

Parent Object: [CustomEventArgs](CustomEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CustomEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customEventArgs\_var" is a variable referencing a CustomEventArgs object. |

"customEventArgs\_var" is a variable referencing a CustomEventArgs object. ```` ``` #include <Core/Application/CustomEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = customEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |