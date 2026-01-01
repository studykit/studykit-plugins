# DistanceAndAngleChamferEdgeSet.objectType Property

Parent Object: [DistanceAndAngleChamferEdgeSet](DistanceAndAngleChamferEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DistanceAndAngleChamferEdgeSet.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"distanceAndAngleChamferEdgeSet\_var" is a variable referencing a DistanceAndAngleChamferEdgeSet object.  ```` ``` # Get the value of the property. propertyValue = distanceAndAngleChamferEdgeSet_var.objectType ``` ```` |

"distanceAndAngleChamferEdgeSet\_var" is a variable referencing a DistanceAndAngleChamferEdgeSet object. ```` ``` #include <Fusion/Features/DistanceAndAngleChamferEdgeSet.h>  // Get the value of the property. string propertyValue = distanceAndAngleChamferEdgeSet_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |