# MarkingMenuEventArgs.firingEvent Property

Parent Object: [MarkingMenuEventArgs](MarkingMenuEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MarkingMenuEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"markingMenuEventArgs\_var" is a variable referencing a MarkingMenuEventArgs object. |

"markingMenuEventArgs\_var" is a variable referencing a MarkingMenuEventArgs object. ```` ``` #include <Core/UserInterface/MarkingMenuEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = markingMenuEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |