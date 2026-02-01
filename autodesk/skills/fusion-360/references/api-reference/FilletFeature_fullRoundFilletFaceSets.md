# FilletFeature.fullRoundFilletFaceSets Property

Parent Object: [FilletFeature](FilletFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeature.h>

## Description

Returns the full round fillet face sets collection associated with this fillet feature. This collection is only valid when the filletFeatureType is FullRoundFilletFeatureType and it returns null if the filletFeatureType is not FullRoundFilletFeatureType.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeature\_var" is a variable referencing a FilletFeature object. |

"filletFeature\_var" is a variable referencing a FilletFeature object. ```` ``` #include <Fusion/Features/FilletFeature.h>  // Get the value of the property. Ptr<FullRoundFilletFaceSets> propertyValue = filletFeature_var->fullRoundFilletFaceSets(); ``` ```` |

## Property Value

This is a read only property whose value is a [FullRoundFilletFaceSets](FullRoundFilletFaceSets.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |