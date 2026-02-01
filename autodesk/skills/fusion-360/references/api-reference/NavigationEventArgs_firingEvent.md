# NavigationEventArgs.firingEvent Property

Parent Object: [NavigationEventArgs](NavigationEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/NavigationEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"navigationEventArgs\_var" is a variable referencing a NavigationEventArgs object. |

"navigationEventArgs\_var" is a variable referencing a NavigationEventArgs object. ```` ``` #include <Core/UserInterface/NavigationEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = navigationEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |