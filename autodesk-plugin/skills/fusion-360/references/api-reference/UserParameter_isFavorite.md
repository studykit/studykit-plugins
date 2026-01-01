# UserParameter.isFavorite Property

Parent Object: [UserParameter](UserParameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/UserParameter.h>

## Description

Gets and sets whether this parameter is included in the Favorites list in the parameters dialog

## Syntax

* [Python](#Python)
* [C++](#C++)

"userParameter\_var" is a variable referencing a UserParameter object. |

"userParameter\_var" is a variable referencing a UserParameter object. ```` ``` #include <Fusion/Fusion/UserParameter.h>  // Get the value of the property. boolean propertyValue = userParameter_var->isFavorite();  // Set the value of the property, where value_var is a boolean. bool returnValue = userParameter_var->isFavorite(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |