# Features.extendFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the Extend features within the component and supports the creation of new Extend features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<ExtendFeatures> propertyValue = features_var->extendFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is an [ExtendFeatures](ExtendFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [extendFeatures.add](extendFeatures_add_Sample.htm) | Demonstrates the extendFeatures.add method. To use this sample, have a design open that contains at least one surface body. When you run the sample, you will be prompted to select an open edge of the body. |
| [Extend Feature API Sample](ExtendFeatureSample_Sample.htm) | Demonstrates creating a new extend feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |