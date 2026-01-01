# UserParameter.unit Property

Parent Object: [UserParameter](UserParameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/UserParameter.h>

## Description

The unit type associated with this parameter. An empty string is returned for parameters that don't have a unit type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userParameter\_var" is a variable referencing a UserParameter object. |

"userParameter\_var" is a variable referencing a UserParameter object. ```` ``` #include <Fusion/Fusion/UserParameter.h>  // Get the value of the property. string propertyValue = userParameter_var->unit(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |