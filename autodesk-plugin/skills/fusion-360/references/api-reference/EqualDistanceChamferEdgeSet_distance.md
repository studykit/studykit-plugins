# EqualDistanceChamferEdgeSet.distance Property

Parent Object: [EqualDistanceChamferEdgeSet](EqualDistanceChamferEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/EqualDistanceChamferEdgeSet.h>

## Description

Returns the model parameter that controls the offset distance of the chamfer. You can edit the distance by using the properties on the returned ModelParameter object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"equalDistanceChamferEdgeSet\_var" is a variable referencing an EqualDistanceChamferEdgeSet object. |

"equalDistanceChamferEdgeSet\_var" is a variable referencing an EqualDistanceChamferEdgeSet object. ```` ``` #include <Fusion/Features/EqualDistanceChamferEdgeSet.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = equalDistanceChamferEdgeSet_var->distance(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |