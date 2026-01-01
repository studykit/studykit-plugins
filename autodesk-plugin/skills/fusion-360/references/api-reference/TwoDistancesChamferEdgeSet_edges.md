# TwoDistancesChamferEdgeSet.edges Property

Parent Object: [TwoDistancesChamferEdgeSet](TwoDistancesChamferEdgeSet.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TwoDistancesChamferEdgeSet.h>

## Description

Gets and sets the edges that will be chamfered. This collection can contain BRepEdge, BRepFace, and Feature objects. If BRepFace or Feature are objects are provided, all of the edges associated with those objects will be chamfered.

## Syntax

* [Python](#Python)
* [C++](#C++)

"twoDistancesChamferEdgeSet\_var" is a variable referencing a TwoDistancesChamferEdgeSet object.  ```` ``` # Get the value of the property. propertyValue = twoDistancesChamferEdgeSet_var.edges  # Set the value of the property. twoDistancesChamferEdgeSet_var.edges = propertyValue ``` ```` |

"twoDistancesChamferEdgeSet\_var" is a variable referencing a TwoDistancesChamferEdgeSet object. ```` ``` #include <Fusion/Features/TwoDistancesChamferEdgeSet.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = twoDistancesChamferEdgeSet_var->edges();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = twoDistancesChamferEdgeSet_var->edges(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |