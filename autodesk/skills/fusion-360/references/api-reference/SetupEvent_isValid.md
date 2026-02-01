# SetupEvent.isValid Property

Parent Object: [SetupEvent](SetupEvent.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupEvent.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupEvent\_var" is a variable referencing a SetupEvent object. |

"setupEvent\_var" is a variable referencing a SetupEvent object. ```` ``` #include <Cam/CAM/SetupEvent.h>  // Get the value of the property. boolean propertyValue = setupEvent_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |