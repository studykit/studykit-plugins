# Features.splitBodyFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the SplitBody features within the component and supports the creation of new SplitBody features

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<SplitBodyFeatures> propertyValue = features_var->splitBodyFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [SplitBodyFeatures](SplitBodyFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [splitBodyFeatures.add](splitBodyfeatures_add_Sample.htm) | Demonstrates the splitBodyFeatures.add method. |
| [Split Body Feature API Sample](SplitBodyFeatureSample_Sample.htm) | Demonstrates creating a new split body feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |