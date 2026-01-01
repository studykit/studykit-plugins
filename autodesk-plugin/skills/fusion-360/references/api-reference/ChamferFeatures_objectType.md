# ChamferFeatures.objectType Property

Parent Object: [ChamferFeatures](ChamferFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeatures\_var" is a variable referencing a ChamferFeatures object.  ```` ``` # Get the value of the property. propertyValue = chamferFeatures_var.objectType ``` ```` |

"chamferFeatures\_var" is a variable referencing a ChamferFeatures object. ```` ``` #include <Fusion/Features/ChamferFeatures.h>  // Get the value of the property. string propertyValue = chamferFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |