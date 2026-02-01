# PatchFeature.groupContinuity Property

Parent Object: [PatchFeature](PatchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeature.h>

## Description

Gets and sets the type of surface continuity to use for all edges when the isGroupEdges property is true. The continuity is used to determine how the patch connects to any B-Rep edges in the boundary. It is ignored for any sketch curves in the boundary. The property defaults to ConnectedSurfaceContinuityType. The value of this property is ignored if the isGroupEdges property is false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeature\_var" is a variable referencing a PatchFeature object.  ```` ``` # Get the value of the property. propertyValue = patchFeature_var.groupContinuity  # Set the value of the property. patchFeature_var.groupContinuity = propertyValue ``` ```` |

"patchFeature\_var" is a variable referencing a PatchFeature object. ```` ``` #include <Fusion/Features/PatchFeature.h>  // Get the value of the property. SurfaceContinuityTypes propertyValue = patchFeature_var->groupContinuity();  // Set the value of the property, where value_var is a SurfaceContinuityTypes. bool returnValue = patchFeature_var->groupContinuity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SurfaceContinuityTypes](SurfaceContinuityTypes.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |