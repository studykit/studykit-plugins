# SharedLink.isPasswordRequired Property

Parent Object: [SharedLink](SharedLink.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/SharedLink.h>

## Description

Gets if a password is required to access the file's web page using the link URL. This property can be set to false to turn off the password requirement. It cannot be set to true. To enable a password, use the setPassword method, which sets the password and has the side effect of setting this property to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sharedLink\_var" is a variable referencing a SharedLink object. |

"sharedLink\_var" is a variable referencing a SharedLink object. ```` ``` #include <Core/Dashboard/SharedLink.h>  // Get the value of the property. boolean propertyValue = sharedLink_var->isPasswordRequired();  // Set the value of the property, where value_var is a boolean. bool returnValue = sharedLink_var->isPasswordRequired(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |