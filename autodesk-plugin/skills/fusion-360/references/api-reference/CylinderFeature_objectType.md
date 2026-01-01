# CylinderFeature.objectType Property

Parent Object: [CylinderFeature](CylinderFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CylinderFeature.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylinderFeature\_var" is a variable referencing a CylinderFeature object.  ```` ``` # Get the value of the property. propertyValue = cylinderFeature_var.objectType ``` ```` |

"cylinderFeature\_var" is a variable referencing a CylinderFeature object. ```` ``` #include <Fusion/Features/CylinderFeature.h>  // Get the value of the property. string propertyValue = cylinderFeature_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |