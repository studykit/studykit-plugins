# ChamferFeature.chamferTypeDefinition Property

Parent Object: [ChamferFeature](ChamferFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeature.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeature\_var" is a variable referencing a ChamferFeature object.  ```` ``` # Get the value of the property. propertyValue = chamferFeature_var.chamferTypeDefinition ``` ```` |

"chamferFeature\_var" is a variable referencing a ChamferFeature object. ```` ``` #include <Fusion/Features/ChamferFeature.h>  // Get the value of the property. Ptr<ChamferTypeDefinition> propertyValue = chamferFeature_var->chamferTypeDefinition(); ``` ```` |

## Property Value

This is a read only property whose value is a [ChamferTypeDefinition](ChamferTypeDefinition.htm).

## Version

Introduced in version November 2014
Retired in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |