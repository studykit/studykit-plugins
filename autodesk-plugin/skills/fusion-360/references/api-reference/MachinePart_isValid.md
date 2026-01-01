# MachinePart.isValid Property

Parent Object: [MachinePart](MachinePart.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Machine/MachinePart.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"machinePart\_var" is a variable referencing a MachinePart object. |

"machinePart\_var" is a variable referencing a MachinePart object. ```` ``` #include <Cam/Machine/MachinePart.h>  // Get the value of the property. boolean propertyValue = machinePart_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |