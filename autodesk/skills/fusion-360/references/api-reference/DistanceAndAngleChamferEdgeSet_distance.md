# DistanceAndAngleChamferEdgeSet.distance Property

Parent Object: [DistanceAndAngleChamferEdgeSet](DistanceAndAngleChamferEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DistanceAndAngleChamferEdgeSet.h>

## Description

Returns the model parameter that controls the offset distance of the chamfer. You can edit the distance by using the properties on the returned ModelParameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"distanceAndAngleChamferEdgeSet\_var" is a variable referencing a DistanceAndAngleChamferEdgeSet object. |

"distanceAndAngleChamferEdgeSet\_var" is a variable referencing a DistanceAndAngleChamferEdgeSet object. ```` ``` #include <Fusion/Features/DistanceAndAngleChamferEdgeSet.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = distanceAndAngleChamferEdgeSet_var->distance(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |