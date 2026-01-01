# PatchFeatures.createInput Method

Parent Object: [PatchFeatures](PatchFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PatchFeatures.h>

## Description

Creates a PatchFeatureInput object. Use properties and methods on the returned PatchFeatureInput object to set other settings. The PatchFeatureInput object is used as input to the add method to create the patch feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"patchFeatures\_var" is a variable referencing a [PatchFeatures](PatchFeatures.htm) object.```` ``` returnValue = patchFeatures_var.createInput(boundaryCurve, operation) ``` ```` |

"patchFeatures\_var" is a variable referencing a [PatchFeatures](PatchFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PatchFeatureInput](PatchFeatureInput.htm) | Returns the newly created PatchFeatureInput object or null if the creation fails. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| boundaryCurve | [Base](Base.htm) | Defines the input geometry that will be used to define the boundary. This can be a sketch profile, a single sketch curve, a single B-Rep edge, an ObjectCollection, or a Path object.   If a single sketch curve or B-Rep edge is an input that is not closed; Fusion will automatically find connected sketch curves or B-Rep edges to define a closed loop.   If an ObjectCollection is an input, it must be a set of curves that define a closed shape.   If a Path is an input, it must define a closed shape. |
| operation | [FeatureOperations](FeatureOperations.htm) | The feature operation to perform. Only 'NewBodyFeatureOperation' and 'NewComponentFeatureOperation' are valid operations for patch features. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [patchFeatures.add](patchFeatures_add_Sample.htm) | Demonstrates the patchFeatures.add method by creating a patch surface on the selected profile. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version July 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |