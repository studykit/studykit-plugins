# UserInterfaceGeneralEventArgs.firingEvent Property

Parent Object: [UserInterfaceGeneralEventArgs](UserInterfaceGeneralEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterfaceGeneralEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterfaceGeneralEventArgs\_var" is a variable referencing a UserInterfaceGeneralEventArgs object. |

"userInterfaceGeneralEventArgs\_var" is a variable referencing a UserInterfaceGeneralEventArgs object. ```` ``` #include <Core/UserInterface/UserInterfaceGeneralEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = userInterfaceGeneralEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |