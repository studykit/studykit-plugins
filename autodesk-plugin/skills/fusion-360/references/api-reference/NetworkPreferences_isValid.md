# NetworkPreferences.isValid Property

Parent Object: [NetworkPreferences](NetworkPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/NetworkPreferences.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"networkPreferences\_var" is a variable referencing a NetworkPreferences object. |

"networkPreferences\_var" is a variable referencing a NetworkPreferences object. ```` ``` #include <Core/Application/NetworkPreferences.h>  // Get the value of the property. boolean propertyValue = networkPreferences_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |