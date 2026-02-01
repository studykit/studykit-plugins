# HoleFeatures.add Method

Parent Object: [HoleFeatures](HoleFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeatures.h>

## Description

Creates a new hole feature based on the information provided by a HoleFeatureInput object. To create a new hole, use one of the createInput functions to define a new input object for the type of hole you want to create. Use the methods and properties on the input object to define any additional input. Once the information is defined on the input object, you can pass it to the Add method to create the hole.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeatures\_var" is a variable referencing a [HoleFeatures](HoleFeatures.htm) object.```` ``` returnValue = holeFeatures_var.add(input) ``` ```` |

"holeFeatures\_var" is a variable referencing a [HoleFeatures](HoleFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [HoleFeature](HoleFeature.htm) | Returns the newly created HoleFeature or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [HoleFeatureInput](HoleFeatureInput.htm) | The HoleFeatureInput object that defines the hole you want to create. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [holeFeatures.add](holeFeatures_add_Sample.htm) | Demonstrates the holeFeatures.add method using the createSimpleInput method. To use this sample, have a design open with a box. Select the face for the hole and two edges to define the position of the hole. |
| [Hole Feature API Sample](HoleFeatureSample_Sample.htm) | Demonstrates creating a new hole feature. |
| [holeFeatures.add with Counterbore](holeFeaturesCounterBore_add_Sample.htm) | Demonstrates the holeFeatures.add method using the createCounterboreInput method. The hole is positioned at the center of the selected edge. |
| [holeFeatures.add with Countersink](holeFeaturesCounterSink_add_Sample.htm) | Demonstrates the holeFeatures.add method using the createCountersinkInput method and postions the hole in the center of a selected circular edge. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |