# CylinderFeatures.objectType Property

Parent Object: [CylinderFeatures](CylinderFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CylinderFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cylinderFeatures\_var" is a variable referencing a CylinderFeatures object.  ```` ``` # Get the value of the property. propertyValue = cylinderFeatures_var.objectType ``` ```` |

"cylinderFeatures\_var" is a variable referencing a CylinderFeatures object. ```` ``` #include <Fusion/Features/CylinderFeatures.h>  // Get the value of the property. string propertyValue = cylinderFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |