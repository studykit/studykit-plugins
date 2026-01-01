# ChamferFeatureInput.objectType Property

Parent Object: [ChamferFeatureInput](ChamferFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeatureInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeatureInput\_var" is a variable referencing a ChamferFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = chamferFeatureInput_var.objectType ``` ```` |

"chamferFeatureInput\_var" is a variable referencing a ChamferFeatureInput object. ```` ``` #include <Fusion/Features/ChamferFeatureInput.h>  // Get the value of the property. string propertyValue = chamferFeatureInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |