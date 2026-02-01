# PatchFeature.boundaryCurve Property

Parent Object: [PatchFeature](PatchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeature.h>

## Description

Returns an ObjectCollection that contains all of the sketch curves or B-Rep edges that defines the closed outer boundary of the patch feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeature\_var" is a variable referencing a PatchFeature object.  ```` ``` # Get the value of the property. propertyValue = patchFeature_var.boundaryCurve  # Set the value of the property. patchFeature_var.boundaryCurve = propertyValue ``` ```` |

"patchFeature\_var" is a variable referencing a PatchFeature object. ```` ``` #include <Fusion/Features/PatchFeature.h>  // Get the value of the property. Ptr<Base> propertyValue = patchFeature_var->boundaryCurve();  // Set the value of the property, where value_var is a Base. bool returnValue = patchFeature_var->boundaryCurve(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |