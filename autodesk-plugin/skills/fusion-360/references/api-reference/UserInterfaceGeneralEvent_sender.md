# UserInterfaceGeneralEvent.sender Property

Parent Object: [UserInterfaceGeneralEvent](UserInterfaceGeneralEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterfaceGeneralEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterfaceGeneralEvent\_var" is a variable referencing a UserInterfaceGeneralEvent object. |

"userInterfaceGeneralEvent\_var" is a variable referencing a UserInterfaceGeneralEvent object. ```` ``` #include <Core/UserInterface/UserInterfaceGeneralEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = userInterfaceGeneralEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |