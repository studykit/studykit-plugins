# Application.currentUser Property

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

Returns the User that is currently logged in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"application\_var" is a variable referencing an Application object. |

"application\_var" is a variable referencing an Application object. ```` ``` #include <Core/Application/Application.h>  // Get the value of the property. Ptr<User> propertyValue = application_var->currentUser(); ``` ```` |

## Property Value

This is a read only property whose value is a [User](User.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |