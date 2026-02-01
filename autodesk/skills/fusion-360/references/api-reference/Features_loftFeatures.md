# Features.loftFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the existing loft features and supports the creation of new loft features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<LoftFeatures> propertyValue = features_var->loftFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [LoftFeatures](LoftFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [loftFeatures.add](loftFeatures_add_Sample.htm) | Demonstrates the loftFeatures.add method. |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |