# HoleFeature.holeTapType Property

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

This property returns the current type of tap associated with this hole. You can set the tap type by using one of the following methods: setToSimpleHole, setToClearanceHole, or setToTappedHole.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a HoleFeature object. |

"holeFeature\_var" is a variable referencing a HoleFeature object. ```` ``` #include <Fusion/Features/HoleFeature.h>  // Get the value of the property. HoleTapTypes propertyValue = holeFeature_var->holeTapType(); ``` ```` |

## Property Value

This is a read only property whose value is a [HoleTapTypes](HoleTapTypes.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |