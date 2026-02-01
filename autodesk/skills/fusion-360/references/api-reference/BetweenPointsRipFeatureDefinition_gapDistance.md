# BetweenPointsRipFeatureDefinition.gapDistance Property

Parent Object: [BetweenPointsRipFeatureDefinition](BetweenPointsRipFeatureDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/BetweenPointsRipFeatureDefinition.h>

## Description

Gets the ModelParameter that defines the gap distance of the rip. The value can be edited by using the properties of the returned ModelParameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"betweenPointsRipFeatureDefinition\_var" is a variable referencing a BetweenPointsRipFeatureDefinition object. |

"betweenPointsRipFeatureDefinition\_var" is a variable referencing a BetweenPointsRipFeatureDefinition object. ```` ``` #include <Fusion/SheetMetal/BetweenPointsRipFeatureDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = betweenPointsRipFeatureDefinition_var->gapDistance(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |