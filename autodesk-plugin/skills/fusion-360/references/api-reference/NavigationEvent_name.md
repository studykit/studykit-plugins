# NavigationEvent.name Property

Parent Object: [NavigationEvent](NavigationEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/NavigationEvent.h>

## Description

The name of the event - e.g. "DocumentOpening"

## Syntax

* [Python](#Python)
* [C++](#C++)

"navigationEvent\_var" is a variable referencing a NavigationEvent object. |

"navigationEvent\_var" is a variable referencing a NavigationEvent object. ```` ``` #include <Core/UserInterface/NavigationEvent.h>  // Get the value of the property. string propertyValue = navigationEvent_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |