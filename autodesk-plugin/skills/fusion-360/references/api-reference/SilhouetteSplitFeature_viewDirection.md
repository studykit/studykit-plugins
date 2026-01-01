# SilhouetteSplitFeature.viewDirection Property

Parent Object: [SilhouetteSplitFeature](SilhouetteSplitFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SilhouetteSplitFeature.h>

## Description

Gets and sets the entity that defines the silhouette view direction, which can be a construction axis, linear BRepEdge, planar BRepFace or a construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSplitFeature\_var" is a variable referencing a SilhouetteSplitFeature object.  ```` ``` # Get the value of the property. propertyValue = silhouetteSplitFeature_var.viewDirection  # Set the value of the property. silhouetteSplitFeature_var.viewDirection = propertyValue ``` ```` |

"silhouetteSplitFeature\_var" is a variable referencing a SilhouetteSplitFeature object. ```` ``` #include <Fusion/Features/SilhouetteSplitFeature.h>  // Get the value of the property. Ptr<Base> propertyValue = silhouetteSplitFeature_var->viewDirection();  // Set the value of the property, where value_var is a Base. bool returnValue = silhouetteSplitFeature_var->viewDirection(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |