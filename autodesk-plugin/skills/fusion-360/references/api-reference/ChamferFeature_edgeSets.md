# ChamferFeature.edgeSets Property

Parent Object: [ChamferFeature](ChamferFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeature.h>

## Description

Returns the edge sets associated with this chamfer.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeature\_var" is a variable referencing a ChamferFeature object. |

"chamferFeature\_var" is a variable referencing a ChamferFeature object. ```` ``` #include <Fusion/Features/ChamferFeature.h>  // Get the value of the property. Ptr<ChamferEdgeSets> propertyValue = chamferFeature_var->edgeSets(); ``` ```` |

## Property Value

This is a read only property whose value is a [ChamferEdgeSets](ChamferEdgeSets.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |