# Features.reverseNormalFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the Reverse Normal features within the component and supports the creation of new Reverse Normal features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<ReverseNormalFeatures> propertyValue = features_var->reverseNormalFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [ReverseNormalFeatures](ReverseNormalFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [reverseNormalFeatures.add](reverseNormalFeatures_add_Sample.htm) | Demonstrates the reverseNormalFeatures.add method. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |