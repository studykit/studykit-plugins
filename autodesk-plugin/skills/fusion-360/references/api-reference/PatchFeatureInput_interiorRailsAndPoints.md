# PatchFeatureInput.interiorRailsAndPoints Property

Parent Object: [PatchFeatureInput](PatchFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeatureInput.h>

## Description

Gets and sets any interior curves or points the patch should fit through. Valid entities include object collections of connected curves, paths, sketch curves, sketch points, B-Rep edges, and construction points.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = patchFeatureInput_var.interiorRailsAndPoints  # Set the value of the property. patchFeatureInput_var.interiorRailsAndPoints = propertyValue ``` ```` |

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object. ```` ``` #include <Fusion/Features/PatchFeatureInput.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = patchFeatureInput_var->interiorRailsAndPoints();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = patchFeatureInput_var->interiorRailsAndPoints(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |