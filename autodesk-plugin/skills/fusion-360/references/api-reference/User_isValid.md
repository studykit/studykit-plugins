# User.isValid Property

Parent Object: [User](User.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/User.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"user\_var" is a variable referencing a User object. |

"user\_var" is a variable referencing a User object. ```` ``` #include <Core/Application/User.h>  // Get the value of the property. boolean propertyValue = user_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |