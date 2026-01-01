# Status.isValid Property

Parent Object: [Status](Status.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Status.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"status\_var" is a variable referencing a Status object. |

"status\_var" is a variable referencing a Status object. ```` ``` #include <Core/Application/Status.h>  // Get the value of the property. boolean propertyValue = status_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |