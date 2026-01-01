# CommandEventArgs.firingEvent Property

Parent Object: [CommandEventArgs](CommandEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandEventArgs\_var" is a variable referencing a CommandEventArgs object. |

"commandEventArgs\_var" is a variable referencing a CommandEventArgs object. ```` ``` #include <Core/UserInterface/CommandEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = commandEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |