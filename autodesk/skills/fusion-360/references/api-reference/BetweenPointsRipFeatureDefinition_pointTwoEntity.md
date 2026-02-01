# BetweenPointsRipFeatureDefinition.pointTwoEntity Property

Parent Object: [BetweenPointsRipFeatureDefinition](BetweenPointsRipFeatureDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/BetweenPointsRipFeatureDefinition.h>

## Description

Gets and sets the BRepEdge or BRepVertex that defines the second point for a between points rip. If a BRepEdge is returned the pointTwoOffset property will control the position of the point along the edge.

## Syntax

* [Python](#Python)
* [C++](#C++)

"betweenPointsRipFeatureDefinition\_var" is a variable referencing a BetweenPointsRipFeatureDefinition object. |

"betweenPointsRipFeatureDefinition\_var" is a variable referencing a BetweenPointsRipFeatureDefinition object. ```` ``` #include <Fusion/SheetMetal/BetweenPointsRipFeatureDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = betweenPointsRipFeatureDefinition_var->pointTwoEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = betweenPointsRipFeatureDefinition_var->pointTwoEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |