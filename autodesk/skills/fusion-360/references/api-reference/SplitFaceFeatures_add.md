# SplitFaceFeatures.add Method

Parent Object: [SplitFaceFeatures](SplitFaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeatures.h>

## Description

Creates a new split face feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeatures\_var" is a variable referencing a [SplitFaceFeatures](SplitFaceFeatures.htm) object.```` ``` returnValue = splitFaceFeatures_var.add(input) ``` ```` |

"splitFaceFeatures\_var" is a variable referencing a [SplitFaceFeatures](SplitFaceFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SplitFaceFeature](SplitFaceFeature.htm) | Returns the newly created SplitFaceFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [SplitFaceFeatureInput](SplitFaceFeatureInput.htm) | A SplitFaceFeatureInput object that defines the desired split face feature. Use the createInput method to create a new SplitFaceFeatureInput object and then use methods on it (the SplitFaceFeatureInput object) to define the split face. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [splitFaceFeatures.add](splitFaceFeatures_add_Sample.htm) | Demonstrates the splitFaceFeatures.add method by spliting a face with another intersecting face. |
| [Split Face Feature API Sample](SplitFaceFeatureSample_Sample.htm) | Demonstrates creating a new split face feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |