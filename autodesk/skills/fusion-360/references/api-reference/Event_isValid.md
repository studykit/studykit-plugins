# Event.isValid Property

Parent Object: [Event](Event.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Event.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"event\_var" is a variable referencing an Event object. |

"event\_var" is a variable referencing an Event object. ```` ``` #include <Core/Application/Event.h>  // Get the value of the property. boolean propertyValue = event_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |