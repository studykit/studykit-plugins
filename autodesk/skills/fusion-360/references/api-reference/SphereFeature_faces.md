# SphereFeature.faces Property

Parent Object: [SphereFeature](SphereFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SphereFeature.h>

## Description

Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sphereFeature\_var" is a variable referencing a SphereFeature object.  ```` ``` # Get the value of the property. propertyValue = sphereFeature_var.faces ``` ```` |

"sphereFeature\_var" is a variable referencing a SphereFeature object. ```` ``` #include <Fusion/Features/SphereFeature.h>  // Get the value of the property. Ptr<BRepFaces> propertyValue = sphereFeature_var->faces(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFaces](BRepFaces.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |