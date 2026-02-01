# TwoDistancesChamferEdgeSet.distanceTwo Property

Parent Object: [TwoDistancesChamferEdgeSet](TwoDistancesChamferEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TwoDistancesChamferEdgeSet.h>

## Description

Returns the model parameter that controls the first offset distance of the chamfer. You can edit the distance by using the properties on the returned ModelParameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"twoDistancesChamferEdgeSet\_var" is a variable referencing a TwoDistancesChamferEdgeSet object. |

"twoDistancesChamferEdgeSet\_var" is a variable referencing a TwoDistancesChamferEdgeSet object. ```` ``` #include <Fusion/Features/TwoDistancesChamferEdgeSet.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = twoDistancesChamferEdgeSet_var->distanceTwo(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |