# Features.ripFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the existing Rip features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<RipFeatures> propertyValue = features_var->ripFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [RipFeatures](RipFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Rip Feature Sample](RipFeatureSample_Sample.htm) | Demonstrates creating a new sheet metal rip feature. |

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |