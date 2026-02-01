# ThreadFeatures.add Method

Parent Object: [ThreadFeatures](ThreadFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThreadFeatures.h>

## Description

Creates a new thread feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"threadFeatures\_var" is a variable referencing a [ThreadFeatures](ThreadFeatures.htm) object.```` ``` returnValue = threadFeatures_var.add(input) ``` ```` |

"threadFeatures\_var" is a variable referencing a [ThreadFeatures](ThreadFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ThreadFeature](ThreadFeature.htm) | Returns the newly created ThreadFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [ThreadFeatureInput](ThreadFeatureInput.htm) | A ThreadFeatureInput object that defines the desired thread. Use the createInput method to create a new ThreadFeatureInput object and then use methods on it (the ThreadFeatureInput object) to define the thread. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Thread Feature API Sample](ThreadFeatureSample_Sample.htm) | Demonstrates creating a new thread feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |