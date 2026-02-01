# Features.scaleFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the scale features within the component and supports the creation of new scale features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<ScaleFeatures> propertyValue = features_var->scaleFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [ScaleFeatures](ScaleFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [scaleFeatures.add](scaleFeatures_add_Sample.htm) | Demonstrates the creation a scale feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |