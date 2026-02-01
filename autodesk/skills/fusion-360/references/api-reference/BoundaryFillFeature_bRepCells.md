# BoundaryFillFeature.bRepCells Property

Parent Object: [BoundaryFillFeature](BoundaryFillFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeature.h>

## Description

Gets the set of closed boundaries that have been calculated based on the current set of tools. To get this collection the model must be in the state it was when the feature was initially computed, which means the timeline marker must be positioned to immediately before this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeature\_var" is a variable referencing a BoundaryFillFeature object.  ```` ``` # Get the value of the property. propertyValue = boundaryFillFeature_var.bRepCells ``` ```` |

"boundaryFillFeature\_var" is a variable referencing a BoundaryFillFeature object. ```` ``` #include <Fusion/Features/BoundaryFillFeature.h>  // Get the value of the property. Ptr<BRepCells> propertyValue = boundaryFillFeature_var->bRepCells(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepCells](BRepCells.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |