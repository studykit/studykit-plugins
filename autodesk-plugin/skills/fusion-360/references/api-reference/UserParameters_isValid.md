# UserParameters.isValid Property

Parent Object: [UserParameters](UserParameters.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/UserParameters.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userParameters\_var" is a variable referencing a UserParameters object. |

"userParameters\_var" is a variable referencing a UserParameters object. ```` ``` #include <Fusion/Fusion/UserParameters.h>  // Get the value of the property. boolean propertyValue = userParameters_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |