# CylinderFeature.isSuppressed Property

Parent Object: [CylinderFeature](CylinderFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CylinderFeature.h>

## Description

Gets and sets if this feature is suppressed. This is only valid for parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylinderFeature\_var" is a variable referencing a CylinderFeature object. |

"cylinderFeature\_var" is a variable referencing a CylinderFeature object. ```` ``` #include <Fusion/Features/CylinderFeature.h>  // Get the value of the property. boolean propertyValue = cylinderFeature_var->isSuppressed();  // Set the value of the property, where value_var is a boolean. bool returnValue = cylinderFeature_var->isSuppressed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |