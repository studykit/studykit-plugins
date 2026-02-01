# ScaleFeature.faces Property

Parent Object: [ScaleFeature](ScaleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ScaleFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scaleFeature\_var" is a variable referencing a ScaleFeature object.  ```` ``` # Get the value of the property. propertyValue = scaleFeature_var.faces ``` ```` |

"scaleFeature\_var" is a variable referencing a ScaleFeature object. ```` ``` #include <Fusion/Features/ScaleFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = scaleFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |