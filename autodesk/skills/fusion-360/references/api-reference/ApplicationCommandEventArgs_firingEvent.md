# ApplicationCommandEventArgs.firingEvent Property

Parent Object: [ApplicationCommandEventArgs](ApplicationCommandEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ApplicationCommandEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationCommandEventArgs\_var" is a variable referencing an ApplicationCommandEventArgs object. |

"applicationCommandEventArgs\_var" is a variable referencing an ApplicationCommandEventArgs object. ```` ``` #include <Core/UserInterface/ApplicationCommandEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = applicationCommandEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |