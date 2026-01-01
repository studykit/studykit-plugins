# Features.ruledSurfaceFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the Ruled Surface features within the component and supports the creation of new Ruled Surface features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<RuledSurfaceFeatures> propertyValue = features_var->ruledSurfaceFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [RuledSurfaceFeatures](RuledSurfaceFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Ruled Surface Feature API Sample](RuledSurfaceFeatureSample_Sample.htm) | Demonstrates creating a new ruled surface feature. |

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |