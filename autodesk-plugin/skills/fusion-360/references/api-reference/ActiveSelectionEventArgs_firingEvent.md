# ActiveSelectionEventArgs.firingEvent Property

Parent Object: [ActiveSelectionEventArgs](ActiveSelectionEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ActiveSelectionEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"activeSelectionEventArgs\_var" is a variable referencing an ActiveSelectionEventArgs object. |

"activeSelectionEventArgs\_var" is a variable referencing an ActiveSelectionEventArgs object. ```` ``` #include <Core/UserInterface/ActiveSelectionEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = activeSelectionEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |