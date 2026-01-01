# ChamferFeature.isTangentChain Property

Parent Object: [ChamferFeature](ChamferFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeature.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeature\_var" is a variable referencing a ChamferFeature object.  ```` ``` # Get the value of the property. propertyValue = chamferFeature_var.isTangentChain  # Set the value of the property. chamferFeature_var.isTangentChain = propertyValue ``` ```` |

"chamferFeature\_var" is a variable referencing a ChamferFeature object. ```` ``` #include <Fusion/Features/ChamferFeature.h>  // Get the value of the property. boolean propertyValue = chamferFeature_var->isTangentChain();  // Set the value of the property, where value_var is a boolean. bool returnValue = chamferFeature_var->isTangentChain(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2014
Retired in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |