# BetweenPointsRipFeatureDefinition.pointTwoOffset Property

Parent Object: [BetweenPointsRipFeatureDefinition](BetweenPointsRipFeatureDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/BetweenPointsRipFeatureDefinition.h>

## Description

Gets the ModelParameter that defines the offset for the second point of a between points rip. This is the physical distance from the topological start of the edge. If the offset is either negative, or exceeds the edge length, then the point will be taken as the corresponding vertex of the edge. Returns null if the first point is defined by a vertex. The value can be edited by using the properties of the returned ModelParameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"betweenPointsRipFeatureDefinition\_var" is a variable referencing a BetweenPointsRipFeatureDefinition object. |

"betweenPointsRipFeatureDefinition\_var" is a variable referencing a BetweenPointsRipFeatureDefinition object. ```` ``` #include <Fusion/SheetMetal/BetweenPointsRipFeatureDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = betweenPointsRipFeatureDefinition_var->pointTwoOffset(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |