# ProductUsageData.isTrackingToImproveSoftwareEnabled Property

Parent Object: [ProductUsageData](ProductUsageData.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ProductUsageData.h>

## Description

Gets and sets if data can be collected to help improve the products and services that Autodesk provides. This is the preference setting titled "Help develop our products and services".

## Syntax

* [Python](#Python)
* [C++](#C++)

"productUsageData\_var" is a variable referencing a ProductUsageData object. |

"productUsageData\_var" is a variable referencing a ProductUsageData object. ```` ``` #include <Core/Application/ProductUsageData.h>  // Get the value of the property. boolean propertyValue = productUsageData_var->isTrackingToImproveSoftwareEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = productUsageData_var->isTrackingToImproveSoftwareEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |