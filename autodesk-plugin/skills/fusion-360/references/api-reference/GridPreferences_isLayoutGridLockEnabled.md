# GridPreferences.isLayoutGridLockEnabled Property

Parent Object: [GridPreferences](GridPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GridPreferences.h>

## Description

Gets and sets if the layout grid lock is enabled.

## Syntax

* [Python](#Python)
* [C++](#C++)

"gridPreferences\_var" is a variable referencing a GridPreferences object. |

"gridPreferences\_var" is a variable referencing a GridPreferences object. ```` ``` #include <Core/Application/GridPreferences.h>  // Get the value of the property. boolean propertyValue = gridPreferences_var->isLayoutGridLockEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = gridPreferences_var->isLayoutGridLockEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |