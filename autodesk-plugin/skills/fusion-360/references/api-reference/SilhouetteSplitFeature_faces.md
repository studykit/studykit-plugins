# SilhouetteSplitFeature.faces Property

Parent Object: [SilhouetteSplitFeature](SilhouetteSplitFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SilhouetteSplitFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSplitFeature\_var" is a variable referencing a SilhouetteSplitFeature object.  ```` ``` # Get the value of the property. propertyValue = silhouetteSplitFeature_var.faces ``` ```` |

"silhouetteSplitFeature\_var" is a variable referencing a SilhouetteSplitFeature object. ```` ``` #include <Fusion/Features/SilhouetteSplitFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = silhouetteSplitFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |