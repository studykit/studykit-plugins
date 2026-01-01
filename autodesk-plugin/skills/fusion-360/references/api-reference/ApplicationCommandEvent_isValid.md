# ApplicationCommandEvent.isValid Property

Parent Object: [ApplicationCommandEvent](ApplicationCommandEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ApplicationCommandEvent.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationCommandEvent\_var" is a variable referencing an ApplicationCommandEvent object. |

"applicationCommandEvent\_var" is a variable referencing an ApplicationCommandEvent object. ```` ``` #include <Core/UserInterface/ApplicationCommandEvent.h>  // Get the value of the property. boolean propertyValue = applicationCommandEvent_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |