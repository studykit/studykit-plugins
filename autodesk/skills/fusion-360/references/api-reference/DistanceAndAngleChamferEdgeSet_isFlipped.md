# DistanceAndAngleChamferEdgeSet.isFlipped Property

Parent Object: [DistanceAndAngleChamferEdgeSet](DistanceAndAngleChamferEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DistanceAndAngleChamferEdgeSet.h>

## Description

Gets and sets if the chamfer is flipped. This swaps the directions for distance one and two.

## Syntax

* [Python](#Python)
* [C++](#C++)

"distanceAndAngleChamferEdgeSet\_var" is a variable referencing a DistanceAndAngleChamferEdgeSet object.  ```` ``` # Get the value of the property. propertyValue = distanceAndAngleChamferEdgeSet_var.isFlipped  # Set the value of the property. distanceAndAngleChamferEdgeSet_var.isFlipped = propertyValue ``` ```` |

"distanceAndAngleChamferEdgeSet\_var" is a variable referencing a DistanceAndAngleChamferEdgeSet object. ```` ``` #include <Fusion/Features/DistanceAndAngleChamferEdgeSet.h>  // Get the value of the property. boolean propertyValue = distanceAndAngleChamferEdgeSet_var->isFlipped();  // Set the value of the property, where value_var is a boolean. bool returnValue = distanceAndAngleChamferEdgeSet_var->isFlipped(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |