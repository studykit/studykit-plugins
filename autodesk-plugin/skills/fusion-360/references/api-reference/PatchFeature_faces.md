# PatchFeature.faces Property

Parent Object: [PatchFeature](PatchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeature\_var" is a variable referencing a PatchFeature object.  ```` ``` # Get the value of the property. propertyValue = patchFeature_var.faces ``` ```` |

"patchFeature\_var" is a variable referencing a PatchFeature object. ```` ``` #include <Fusion/Features/PatchFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = patchFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |