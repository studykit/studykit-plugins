# PatchFeature.interiorRailsAndPoints Property

Parent Object: [PatchFeature](PatchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeature.h>

## Description

Gets and sets any interior curves or points the patch should fit through. Valid entities include object collections of connected curves, paths, sketch curves, sketch points, B-Rep edges, and construction points.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeature\_var" is a variable referencing a PatchFeature object.  ```` ``` # Get the value of the property. propertyValue = patchFeature_var.interiorRailsAndPoints  # Set the value of the property. patchFeature_var.interiorRailsAndPoints = propertyValue ``` ```` |

"patchFeature\_var" is a variable referencing a PatchFeature object. ```` ``` #include <Fusion/Features/PatchFeature.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = patchFeature_var->interiorRailsAndPoints();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = patchFeature_var->interiorRailsAndPoints(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |