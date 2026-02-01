# KeyboardEventArgs.firingEvent Property

Parent Object: [KeyboardEventArgs](KeyboardEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/KeyboardEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"keyboardEventArgs\_var" is a variable referencing a KeyboardEventArgs object. |

"keyboardEventArgs\_var" is a variable referencing a KeyboardEventArgs object. ```` ``` #include <Core/UserInterface/KeyboardEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = keyboardEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |