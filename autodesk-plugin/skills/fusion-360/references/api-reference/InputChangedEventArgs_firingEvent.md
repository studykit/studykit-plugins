# InputChangedEventArgs.firingEvent Property

Parent Object: [InputChangedEventArgs](InputChangedEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/InputChangedEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"inputChangedEventArgs\_var" is a variable referencing an InputChangedEventArgs object. |

"inputChangedEventArgs\_var" is a variable referencing an InputChangedEventArgs object. ```` ``` #include <Core/UserInterface/InputChangedEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = inputChangedEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |