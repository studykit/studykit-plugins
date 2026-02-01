# ProductUsageData.objectType Property

Parent Object: [ProductUsageData](ProductUsageData.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ProductUsageData.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"productUsageData\_var" is a variable referencing a ProductUsageData object.  ```` ``` # Get the value of the property. propertyValue = productUsageData_var.objectType ``` ```` |

"productUsageData\_var" is a variable referencing a ProductUsageData object. ```` ``` #include <Core/Application/ProductUsageData.h>  // Get the value of the property. string propertyValue = productUsageData_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |