# ActiveSelectionEvent.isValid Property

Parent Object: [ActiveSelectionEvent](ActiveSelectionEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ActiveSelectionEvent.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"activeSelectionEvent\_var" is a variable referencing an ActiveSelectionEvent object. |

"activeSelectionEvent\_var" is a variable referencing an ActiveSelectionEvent object. ```` ``` #include <Core/UserInterface/ActiveSelectionEvent.h>  // Get the value of the property. boolean propertyValue = activeSelectionEvent_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |