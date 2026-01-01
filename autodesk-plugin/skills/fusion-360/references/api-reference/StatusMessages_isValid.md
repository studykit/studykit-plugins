# StatusMessages.isValid Property

Parent Object: [StatusMessages](StatusMessages.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/StatusMessages.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"statusMessages\_var" is a variable referencing a StatusMessages object. |

"statusMessages\_var" is a variable referencing a StatusMessages object. ```` ``` #include <Core/Application/StatusMessages.h>  // Get the value of the property. boolean propertyValue = statusMessages_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |