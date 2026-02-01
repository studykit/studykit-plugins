# MaterialPreferences.isValid Property

Parent Object: [MaterialPreferences](MaterialPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MaterialPreferences.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materialPreferences\_var" is a variable referencing a MaterialPreferences object. |

"materialPreferences\_var" is a variable referencing a MaterialPreferences object. ```` ``` #include <Core/Application/MaterialPreferences.h>  // Get the value of the property. boolean propertyValue = materialPreferences_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |