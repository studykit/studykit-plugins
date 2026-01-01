# Features.baseFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the existing base features and supports the creation of new base features. A base feature represents a body that is non-parametric.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<BaseFeatures> propertyValue = features_var->baseFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [BaseFeatures](BaseFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [baseFeatures.add](baseFeatures_add_Sample.htm) | Demonstrates the baseFeature.add method. |
| [BaseFeature Sample](BaseFeatureSample_Sample.htm) | Creates a new base feature. |
| [Sketches.addToBaseOrFormFeature](Sketches_addToFormBaseOrFeature_Sample.htm) | Demonstrates the Sketches.addToBaseOrFormFeature method. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |