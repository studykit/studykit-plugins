# DeleteFaceFeature.faces Property

Parent Object: [DeleteFaceFeature](DeleteFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DeleteFaceFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"deleteFaceFeature\_var" is a variable referencing a DeleteFaceFeature object.  ```` ``` # Get the value of the property. propertyValue = deleteFaceFeature_var.faces ``` ```` |

"deleteFaceFeature\_var" is a variable referencing a DeleteFaceFeature object. ```` ``` #include <Fusion/Features/DeleteFaceFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = deleteFaceFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |