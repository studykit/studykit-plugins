# SelectionEvent.sender Property

Parent Object: [SelectionEvent](SelectionEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionEvent\_var" is a variable referencing a SelectionEvent object. |

"selectionEvent\_var" is a variable referencing a SelectionEvent object. ```` ``` #include <Core/UserInterface/SelectionEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = selectionEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |