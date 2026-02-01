# CoilFeature.faces Property

Parent Object: [CoilFeature](CoilFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CoilFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coilFeature\_var" is a variable referencing a CoilFeature object.  ```` ``` # Get the value of the property. propertyValue = coilFeature_var.faces ``` ```` |

"coilFeature\_var" is a variable referencing a CoilFeature object. ```` ``` #include <Fusion/Features/CoilFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = coilFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |