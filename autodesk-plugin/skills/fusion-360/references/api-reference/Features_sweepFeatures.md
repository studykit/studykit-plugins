# Features.sweepFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the sweep features within the component and supports the creation of new sweep features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<SweepFeatures> propertyValue = features_var->sweepFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [SweepFeatures](SweepFeatures.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [sweepFeatures.add](sweepFeatures_add_Sample.htm) | Demonstrates the sweepFeatures.add method. |
| [Sweep with guide rail Feature API Sample](SweepWithGuideRailFeatureSample_Sample.htm) | Demonstrates creating a new Sweep feature that uses a guide rail along with a profile. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |