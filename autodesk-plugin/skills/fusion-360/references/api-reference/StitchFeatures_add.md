# StitchFeatures.add Method

Parent Object: [StitchFeatures](StitchFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeatures.h>

## Description

Creates a new stitch feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stitchFeatures\_var" is a variable referencing a [StitchFeatures](StitchFeatures.htm) object.```` ``` returnValue = stitchFeatures_var.add(input) ``` ```` |

"stitchFeatures\_var" is a variable referencing a [StitchFeatures](StitchFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [StitchFeature](StitchFeature.htm) | Returns the newly created StitchFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [StitchFeatureInput](StitchFeatureInput.htm) | A StitchFeatureInput object that defines the desired stitch feature. Use the createInput method to create a new StitchFeatureInput object and then use methods on it (the StitchFeatureInput object) to define the stitch feature. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [stitchFeatures.add](stitchFeatures_add_Sample.htm) | Demonstrates the stitchFeatures.add method. |
| [Stitch Feature API Sample](StitchFeatureSample_Sample.htm) | Demonstrates creating a new stitch feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |