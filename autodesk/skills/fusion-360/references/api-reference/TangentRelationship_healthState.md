# TangentRelationship.healthState Property

Parent Object: [TangentRelationship](TangentRelationship.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationship.h>

## Description

Returns the current health state of the tangent relationship.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentRelationship\_var" is a variable referencing a TangentRelationship object. |

"tangentRelationship\_var" is a variable referencing a TangentRelationship object. ```` ``` #include <Fusion/Components/TangentRelationship.h>  // Get the value of the property. FeatureHealthStates propertyValue = tangentRelationship_var->healthState(); ``` ```` |

## Property Value

This is a read only property whose value is a [FeatureHealthStates](FeatureHealthStates.htm).

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |