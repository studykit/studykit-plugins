# PatchFeature.continuity Property

Parent Object: [PatchFeature](PatchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeature.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property has been retired and replaced by either the groupContinuity property or setContinuity method, depending on if the isGroupEdges property is true or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeature\_var" is a variable referencing a PatchFeature object.  ```` ``` # Get the value of the property. propertyValue = patchFeature_var.continuity  # Set the value of the property. patchFeature_var.continuity = propertyValue ``` ```` |

"patchFeature\_var" is a variable referencing a PatchFeature object. ```` ``` #include <Fusion/Features/PatchFeature.h>  // Get the value of the property. SurfaceContinuityTypes propertyValue = patchFeature_var->continuity();  // Set the value of the property, where value_var is a SurfaceContinuityTypes. bool returnValue = patchFeature_var->continuity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SurfaceContinuityTypes](SurfaceContinuityTypes.htm).

## Version

Introduced in version July 2016
Retired in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |