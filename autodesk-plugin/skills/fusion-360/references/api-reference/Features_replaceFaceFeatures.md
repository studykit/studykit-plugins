# Features.replaceFaceFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the replaceFace features within the component and supports the creation of new replaceFace features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<ReplaceFaceFeatures> propertyValue = features_var->replaceFaceFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [ReplaceFaceFeatures](ReplaceFaceFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [replaceFaceFeatures.add](replaceFaceFeatures_add_Sample.htm) | Demonstrate the remove replaceFaceFeatures.add method. |
| [ReplaceFace Feature](ReplaceFaceFeatureSample_Sample.htm) | Demonstrates creating a new replaceface feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |