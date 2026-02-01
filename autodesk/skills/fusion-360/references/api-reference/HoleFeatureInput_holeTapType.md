# HoleFeatureInput.holeTapType Property

Parent Object: [HoleFeatureInput](HoleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeatureInput.h>

## Description

Returns the current type of tap associated with this hole. When a new HoleFeatureInput is created, this will default to SimpleHoleTapType, which means the hole will not have any tap and will be a simple hole. You can set the tap type by using one of the methods to define the specific tap desired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeatureInput\_var" is a variable referencing a HoleFeatureInput object. |

"holeFeatureInput\_var" is a variable referencing a HoleFeatureInput object. ```` ``` #include <Fusion/Features/HoleFeatureInput.h>  // Get the value of the property. HoleTapTypes propertyValue = holeFeatureInput_var->holeTapType(); ``` ```` |

## Property Value

This is a read only property whose value is a [HoleTapTypes](HoleTapTypes.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |