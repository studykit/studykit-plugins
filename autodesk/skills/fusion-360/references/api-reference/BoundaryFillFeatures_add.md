# BoundaryFillFeatures.add Method

Parent Object: [BoundaryFillFeatures](BoundaryFillFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/BoundaryFillFeatures.h>

## Description

Creates a new boundary fill feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boundaryFillFeatures\_var" is a variable referencing a [BoundaryFillFeatures](BoundaryFillFeatures.htm) object.```` ``` returnValue = boundaryFillFeatures_var.add(input) ``` ```` |

"boundaryFillFeatures\_var" is a variable referencing a [BoundaryFillFeatures](BoundaryFillFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BoundaryFillFeature](BoundaryFillFeature.htm) | Returns the newly created BoundaryFillFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [BoundaryFillFeatureInput](BoundaryFillFeatureInput.htm) | A BoundaryFillFeatureInput object that defines the desired boundary fill feature. Use the createInput method to create a new BoundaryFillFeatureInput object and then use methods on it (the BoundaryFillFeatureInput object) to define the boundary fill feature. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [boundaryFillFeatures.add](boundaryFillFeatures_add_Sample.htm) | Demonstrates the boundaryFill.add method. To use this sample you need to have two existing overlapping bodies. You'll be prompted to select the bodies when running the script. |
| [Boundary Fill Feature API Sample](BoundaryFillFeatureSample_Sample.htm) | Demonstrates creating a new boundary fill feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |