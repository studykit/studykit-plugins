# ChamferFeature.faces Property

Parent Object: [ChamferFeature](ChamferFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeature\_var" is a variable referencing a ChamferFeature object.  ```` ``` # Get the value of the property. propertyValue = chamferFeature_var.faces ``` ```` |

"chamferFeature\_var" is a variable referencing a ChamferFeature object. ```` ``` #include <Fusion/Features/ChamferFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = chamferFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |