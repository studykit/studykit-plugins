# MarkingMenuEvent.isValid Property

Parent Object: [MarkingMenuEvent](MarkingMenuEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MarkingMenuEvent.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"markingMenuEvent\_var" is a variable referencing a MarkingMenuEvent object. |

"markingMenuEvent\_var" is a variable referencing a MarkingMenuEvent object. ```` ``` #include <Core/UserInterface/MarkingMenuEvent.h>  // Get the value of the property. boolean propertyValue = markingMenuEvent_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |