# User.displayName Property

Parent Object: [User](User.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/User.h>

## Description

Returns display name of the user. (i.e. the name that shows up in the Fusion UI)

## Syntax

* [Python](#Python)
* [C++](#C++)

"user\_var" is a variable referencing a User object. |

"user\_var" is a variable referencing a User object. ```` ``` #include <Core/Application/User.h>  // Get the value of the property. string propertyValue = user_var->displayName(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |