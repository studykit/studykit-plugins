# DraftFeatures.add Method

Parent Object: [DraftFeatures](DraftFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeatures.h>

## Description

Creates a new draft feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"draftFeatures\_var" is a variable referencing a [DraftFeatures](DraftFeatures.htm) object.```` ``` returnValue = draftFeatures_var.add(input) ``` ```` |

"draftFeatures\_var" is a variable referencing a [DraftFeatures](DraftFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DraftFeature](DraftFeature.htm) | Returns the newly created DraftFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [DraftFeatureInput](DraftFeatureInput.htm) | A DraftFeatureInput object that defines the desired draft. Use the createInput method to create a new DraftFeatureInput object and then use methods on it (the DraftFeatureInput object) to define the draft. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [draftFeatures.add](draftFeatures_add_Sample.htm) | Demonstrates the draftFeatures.add method. To use this sample, have a design open that contains at least one body. When you run the sample, you will be prompted to select the face to draft. Because the pull direction is using the base X-Y plane, you need to select a face that is not parallel to the X-Y plane. |
| [Draft Feature API Sample](DraftFeatureSample_Sample.htm) | Demonstrates creating a new draft feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |