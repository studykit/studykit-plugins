# MouseEvent.name Property

Parent Object: [MouseEvent](MouseEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MouseEvent.h>

## Description

The name of the event - e.g. "DocumentOpening"

## Syntax

* [Python](#Python)
* [C++](#C++)

"mouseEvent\_var" is a variable referencing a MouseEvent object. |

"mouseEvent\_var" is a variable referencing a MouseEvent object. ```` ``` #include <Core/UserInterface/MouseEvent.h>  // Get the value of the property. string propertyValue = mouseEvent_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |