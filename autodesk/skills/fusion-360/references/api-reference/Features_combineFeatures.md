# Features.combineFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the combine features within the component and supports the creation of new combine features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<CombineFeatures> propertyValue = features_var->combineFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [CombineFeatures](CombineFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [combineFeatures.add](combineFeatures_add_Sample.htm) | Demonstrates the combineFeatures.add method. To use this sample, have a design open that contains at least two bodies. When you run the sample, you will be prompted to select the bodies and they will joined. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |