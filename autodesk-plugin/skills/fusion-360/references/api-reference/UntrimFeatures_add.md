# UntrimFeatures.add Method

Parent Object: [UntrimFeatures](UntrimFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeatures.h>

## Description

Creates a new Untrim feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"untrimFeatures\_var" is a variable referencing a [UntrimFeatures](UntrimFeatures.htm) object.```` ``` returnValue = untrimFeatures_var.add(input) ``` ```` |

"untrimFeatures\_var" is a variable referencing a [UntrimFeatures](UntrimFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [UntrimFeature](UntrimFeature.htm) | Returns the newly created UntrimFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [UntrimFeatureInput](UntrimFeatureInput.htm) | An UntrimFeatureInput object that defines the desired Untrim feature. Use the createInput method to create a new UntrimFeatureInput object and then use methods on it (the UntrimFeatureInput object) to define the desired options for the Untrim feature. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Untrim Feature API Sample](UntrimFeatureSample_Sample.htm) | Demonstrates creating a new untrim feature. |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |