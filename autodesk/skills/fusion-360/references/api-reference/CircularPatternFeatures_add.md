# CircularPatternFeatures.add Method

Parent Object: [CircularPatternFeatures](CircularPatternFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeatures.h>

## Description

Creates a new circular pattern feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeatures\_var" is a variable referencing a [CircularPatternFeatures](CircularPatternFeatures.htm) object.```` ``` returnValue = circularPatternFeatures_var.add(input) ``` ```` |

"circularPatternFeatures\_var" is a variable referencing a [CircularPatternFeatures](CircularPatternFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CircularPatternFeature](CircularPatternFeature.htm) | Returns the newly created CircularPatternFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [CircularPatternFeatureInput](CircularPatternFeatureInput.htm) | A CircularPatternFeatureInput object that defines the desired circular pattern. Use the createInput method to create a new CircularPatternFeatureInput object and then use methods on it (the CircularPatternFeatureInput object) to define the circular pattern. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [circularPatternFeatures.add](circularPatternFeatures_add_Sample.htm) | Demonstrates the circularPatternFeatures.add method. To use the sample have a design open that contains at least one body. When you run the script, it will prompt you to select a body, which will be patterned around the base Y-axis. |
| [CircularPattern Feature API Sample](CircularPatternFeatureSample_Sample.htm) | Demonstrates creating a new circular pattern feature. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |