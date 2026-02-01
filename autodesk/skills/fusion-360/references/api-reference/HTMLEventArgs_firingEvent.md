# HTMLEventArgs.firingEvent Property

Parent Object: [HTMLEventArgs](HTMLEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/HTMLEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"hTMLEventArgs\_var" is a variable referencing a HTMLEventArgs object. |

"hTMLEventArgs\_var" is a variable referencing a HTMLEventArgs object. ```` ``` #include <Core/UserInterface/HTMLEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = hTMLEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |