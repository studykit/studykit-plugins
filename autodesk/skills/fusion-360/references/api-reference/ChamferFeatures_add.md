# ChamferFeatures.add Method

Parent Object: [ChamferFeatures](ChamferFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeatures.h>

## Description

Creates a new chamfer feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeatures\_var" is a variable referencing a [ChamferFeatures](ChamferFeatures.htm) object.```` ``` returnValue = chamferFeatures_var.add(input) ``` ```` |

"chamferFeatures\_var" is a variable referencing a [ChamferFeatures](ChamferFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ChamferFeature](ChamferFeature.htm) | Returns the newly created ChamferFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [ChamferFeatureInput](ChamferFeatureInput.htm) | A ChamferFeatureInput object that defines the desired chamfer. Use the createInput method to create a new ChamferFeatureInput object and then use methods on it (the ChamferFeatureInput object) to define the chamfer. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [chamferFeatures.add](chamferFeatures_add_Sample.htm) | Demonstrates the chamferFeatures.add method. To use this sample have a part open that contains a body. When you run the script, you will be prompted to select an edge to chamfer. |
| [Equal Distance Chamfer Feature API Sample](EqualDistanceChamferFeature_Sample.htm) | Creates an equal distance chamfer on the selected edge. If there are tangent contiguous edges that will also be included in the chamfer. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |