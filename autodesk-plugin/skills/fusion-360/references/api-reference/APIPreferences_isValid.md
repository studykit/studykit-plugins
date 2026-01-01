# APIPreferences.isValid Property

Parent Object: [APIPreferences](APIPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/APIPreferences.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"aPIPreferences\_var" is a variable referencing an APIPreferences object. |

"aPIPreferences\_var" is a variable referencing an APIPreferences object. ```` ``` #include <Core/Application/APIPreferences.h>  // Get the value of the property. boolean propertyValue = aPIPreferences_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |