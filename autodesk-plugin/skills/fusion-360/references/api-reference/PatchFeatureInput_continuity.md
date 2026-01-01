# PatchFeatureInput.continuity Property

Parent Object: [PatchFeatureInput](PatchFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeatureInput.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property has been retired and replaced by either the groupContinuity property or setContinuity method, depending on if the isGroupEdges property is true or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = patchFeatureInput_var.continuity  # Set the value of the property. patchFeatureInput_var.continuity = propertyValue ``` ```` |

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object. ```` ``` #include <Fusion/Features/PatchFeatureInput.h>  // Get the value of the property. SurfaceContinuityTypes propertyValue = patchFeatureInput_var->continuity();  // Set the value of the property, where value_var is a SurfaceContinuityTypes. bool returnValue = patchFeatureInput_var->continuity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SurfaceContinuityTypes](SurfaceContinuityTypes.htm).

## Version

Introduced in version July 2016
Retired in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |