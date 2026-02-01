# ChamferFeatureInput.chamferEdgeSets Property

Parent Object: [ChamferFeatureInput](ChamferFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ChamferFeatureInput.h>

## Description

Returns the collection of edge sets for this chamfer feature input.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chamferFeatureInput\_var" is a variable referencing a ChamferFeatureInput object. |

"chamferFeatureInput\_var" is a variable referencing a ChamferFeatureInput object. ```` ``` #include <Fusion/Features/ChamferFeatureInput.h>  // Get the value of the property. Ptr<ChamferEdgeSets> propertyValue = chamferFeatureInput_var->chamferEdgeSets(); ``` ```` |

## Property Value

This is a read only property whose value is a [ChamferEdgeSets](ChamferEdgeSets.htm).

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