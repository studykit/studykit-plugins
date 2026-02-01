# SilhouetteSplitFeatureInput.viewDirection Property

Parent Object: [SilhouetteSplitFeatureInput](SilhouetteSplitFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SilhouetteSplitFeatureInput.h>

## Description

Gets and sets the entity that defines the silhouette view direction, which can be a construction axis, linear BRepEdge, planar BRepFace or a construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSplitFeatureInput\_var" is a variable referencing a SilhouetteSplitFeatureInput object. |

"silhouetteSplitFeatureInput\_var" is a variable referencing a SilhouetteSplitFeatureInput object. ```` ``` #include <Fusion/Features/SilhouetteSplitFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = silhouetteSplitFeatureInput_var->viewDirection();  // Set the value of the property, where value_var is a Base. bool returnValue = silhouetteSplitFeatureInput_var->viewDirection(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |