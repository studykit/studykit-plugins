# ThickenFeatures.add Method

Parent Object: [ThickenFeatures](ThickenFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeatures.h>

## Description

Creates a new Thicken feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"thickenFeatures\_var" is a variable referencing a [ThickenFeatures](ThickenFeatures.htm) object.```` ``` returnValue = thickenFeatures_var.add(input) ``` ```` |

"thickenFeatures\_var" is a variable referencing a [ThickenFeatures](ThickenFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ThickenFeature](ThickenFeature.htm) | Returns the newly created ThickenFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [ThickenFeatureInput](ThickenFeatureInput.htm) | A FeatureInput object that defines the desired Thicken feature. Use the createInput method to create a new ThickenFeatureInput object and then use methods on it (the ThickenFeatureInput object) to define the Thicken feature. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [thickenFeatures.add](thickenFeatures_add_Sample.htm) | Demonstrates the thickenFeatures.add method. |
| [Thicken Feature API Sample](ThickenFeatureSample_Sample.htm) | Demonstrates creating a new thiken feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |