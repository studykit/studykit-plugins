# MouseEvent.sender Property

Parent Object: [MouseEvent](MouseEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MouseEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mouseEvent\_var" is a variable referencing a MouseEvent object. |

"mouseEvent\_var" is a variable referencing a MouseEvent object. ```` ``` #include <Core/UserInterface/MouseEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = mouseEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |