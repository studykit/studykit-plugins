# ApplicationEventArgs.firingEvent Property

Parent Object: [ApplicationEventArgs](ApplicationEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ApplicationEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationEventArgs\_var" is a variable referencing an ApplicationEventArgs object. |

"applicationEventArgs\_var" is a variable referencing an ApplicationEventArgs object. ```` ``` #include <Core/Application/ApplicationEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = applicationEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |