# HoleFeature.clearanceHoleInfo Property

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

Returns the information used to define a clearance hole. This returns a ClearanceHoleInfo object when the holeTapType returns ClearanceHoleTapType. Otherwise this property returns null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a HoleFeature object. |

"holeFeature\_var" is a variable referencing a HoleFeature object. ```` ``` #include <Fusion/Features/HoleFeature.h>  // Get the value of the property. Ptr<ClearanceHoleInfo> propertyValue = holeFeature_var->clearanceHoleInfo(); ``` ```` |

## Property Value

This is a read only property whose value is a [ClearanceHoleInfo](ClearanceHoleInfo.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |