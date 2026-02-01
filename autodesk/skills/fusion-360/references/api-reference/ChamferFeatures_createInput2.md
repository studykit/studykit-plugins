# ChamferFeatures.createInput2 Method

Parent Object: [ChamferFeatures](ChamferFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeatures.h>

## Description

Creates a ChamferFeatureInput object. Use properties and methods on this object to define the chamfer you want to create and then use the Add method, passing in the ChamferFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeatures\_var" is a variable referencing a [ChamferFeatures](ChamferFeatures.htm) object.```` ``` returnValue = chamferFeatures_var.createInput2() ``` ```` |

"chamferFeatures\_var" is a variable referencing a [ChamferFeatures](ChamferFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ChamferFeatureInput](ChamferFeatureInput.htm) | Returns the newly created ChamferFeatureInput object or null if the creation failed. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [chamferFeatures.add](chamferFeatures_add_Sample.htm) | Demonstrates the chamferFeatures.add method. To use this sample have a part open that contains a body. When you run the script, you will be prompted to select an edge to chamfer. |
| [Equal Distance Chamfer Feature API Sample](EqualDistanceChamferFeature_Sample.htm) | Creates an equal distance chamfer on the selected edge. If there are tangent contiguous edges that will also be included in the chamfer. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |