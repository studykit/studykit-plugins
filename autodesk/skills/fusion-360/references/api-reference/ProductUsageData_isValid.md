# ProductUsageData.isValid Property

Parent Object: [ProductUsageData](ProductUsageData.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ProductUsageData.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"productUsageData\_var" is a variable referencing a ProductUsageData object. |

"productUsageData\_var" is a variable referencing a ProductUsageData object. ```` ``` #include <Core/Application/ProductUsageData.h>  // Get the value of the property. boolean propertyValue = productUsageData_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |