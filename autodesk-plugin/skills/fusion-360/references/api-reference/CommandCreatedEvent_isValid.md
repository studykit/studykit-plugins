# CommandCreatedEvent.isValid Property

Parent Object: [CommandCreatedEvent](CommandCreatedEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandCreatedEvent.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandCreatedEvent\_var" is a variable referencing a CommandCreatedEvent object. |

"commandCreatedEvent\_var" is a variable referencing a CommandCreatedEvent object. ```` ``` #include <Core/UserInterface/CommandCreatedEvent.h>  // Get the value of the property. boolean propertyValue = commandCreatedEvent_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |