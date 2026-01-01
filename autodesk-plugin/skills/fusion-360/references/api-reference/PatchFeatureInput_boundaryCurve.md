# PatchFeatureInput.boundaryCurve Property

Parent Object: [PatchFeatureInput](PatchFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeatureInput.h>

## Description

Gets and sets the input geometry that will be used to define the boundary. This can be a sketch profile, a single sketch curve, a single B-Rep edge, an ObjectCollection, or a Path object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = patchFeatureInput_var.boundaryCurve  # Set the value of the property. patchFeatureInput_var.boundaryCurve = propertyValue ``` ```` |

"patchFeatureInput\_var" is a variable referencing a PatchFeatureInput object. ```` ``` #include <Fusion/Features/PatchFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = patchFeatureInput_var->boundaryCurve();  // Set the value of the property, where value_var is a Base. bool returnValue = patchFeatureInput_var->boundaryCurve(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |