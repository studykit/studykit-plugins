# ProductPreferences.isValid Property

Parent Object: [ProductPreferences](ProductPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ProductPreferences.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"productPreferences\_var" is a variable referencing a ProductPreferences object. |

"productPreferences\_var" is a variable referencing a ProductPreferences object. ```` ``` #include <Core/Application/ProductPreferences.h>  // Get the value of the property. boolean propertyValue = productPreferences_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |