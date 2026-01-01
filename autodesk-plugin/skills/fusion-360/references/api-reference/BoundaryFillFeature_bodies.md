# BoundaryFillFeature.bodies Property

Parent Object: [BoundaryFillFeature](BoundaryFillFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeature.h>

## Description

Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeature\_var" is a variable referencing a BoundaryFillFeature object.  ```` ``` # Get the value of the property. propertyValue = boundaryFillFeature_var.bodies ``` ```` |

"boundaryFillFeature\_var" is a variable referencing a BoundaryFillFeature object. ```` ``` #include <Fusion/Features/BoundaryFillFeature.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = boundaryFillFeature_var->bodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |