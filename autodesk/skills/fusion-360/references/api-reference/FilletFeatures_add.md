# FilletFeatures.add Method

Parent Object: [FilletFeatures](FilletFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletFeatures.h>

## Description

Creates a new fillet feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletFeatures\_var" is a variable referencing a [FilletFeatures](FilletFeatures.htm) object.```` ``` returnValue = filletFeatures_var.add(input) ``` ```` |

"filletFeatures\_var" is a variable referencing a [FilletFeatures](FilletFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [FilletFeature](FilletFeature.htm) | Returns the newly created FilletFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [FilletFeatureInput](FilletFeatureInput.htm) | A FilletFeatureInput object that defines the desired fillet. Use the createInput method to create a new FilletFeatureInput object and then use methods on it (the FilletFeatureInput object) to define the fillet. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Constant Radius Fillet API Sample](ConstantRadiusFillet_Sample.htm) | Creates a constant radius fillet on the selected edge. If there are tangent contiguous edges that will also be included in the fillet. |
| [filletFeatures.add](filletFeatures_add_Sample.htm) | Demonstrates the filletFeatures.add method. |
| [Fillet Feature API Sample](FilletFeatureSample_Sample.htm) | Demonstrates creating fillets using the various types of fillets. Create a new design and add a box that is at least 2 cm on each side. The script creates a constant radius, variable radius and chord length fillets. After creating each one, it deletes it and then creates the next. To see any of the fillets that were deleted, undo to get the fillet back. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |