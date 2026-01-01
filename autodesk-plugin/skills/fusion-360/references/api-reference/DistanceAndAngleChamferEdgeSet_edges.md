# DistanceAndAngleChamferEdgeSet.edges Property

Parent Object: [DistanceAndAngleChamferEdgeSet](DistanceAndAngleChamferEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DistanceAndAngleChamferEdgeSet.h>

## Description

Gets and sets the edges that will be chamfered. This collection can contain BRepEdge, BRepFace, and Feature objects. If BRepFace or Feature are objects are provided, all of the edges associated with those objects will be chamfered.

## Syntax

* [Python](#Python)
* [C++](#C++)

"distanceAndAngleChamferEdgeSet\_var" is a variable referencing a DistanceAndAngleChamferEdgeSet object.  ```` ``` # Get the value of the property. propertyValue = distanceAndAngleChamferEdgeSet_var.edges  # Set the value of the property. distanceAndAngleChamferEdgeSet_var.edges = propertyValue ``` ```` |

"distanceAndAngleChamferEdgeSet\_var" is a variable referencing a DistanceAndAngleChamferEdgeSet object. ```` ``` #include <Fusion/Features/DistanceAndAngleChamferEdgeSet.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = distanceAndAngleChamferEdgeSet_var->edges();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = distanceAndAngleChamferEdgeSet_var->edges(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |