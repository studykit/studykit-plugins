# MouseEventArgs.firingEvent Property

Parent Object: [MouseEventArgs](MouseEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MouseEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mouseEventArgs\_var" is a variable referencing a MouseEventArgs object. |

"mouseEventArgs\_var" is a variable referencing a MouseEventArgs object. ```` ``` #include <Core/UserInterface/MouseEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = mouseEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |