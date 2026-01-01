# SweepFeatures.add Method

Parent Object: [SweepFeatures](SweepFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatures.h>

## Description

Creates a new sweep feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatures\_var" is a variable referencing a [SweepFeatures](SweepFeatures.htm) object.```` ``` returnValue = sweepFeatures_var.add(input) ``` ```` |

"sweepFeatures\_var" is a variable referencing a [SweepFeatures](SweepFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SweepFeature](SweepFeature.htm) | Returns the newly created SweepFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [SweepFeatureInput](SweepFeatureInput.htm) | A SweepFeatureInput object that defines the desired sweep. Use the createInput method to create a new SweepFeatureInput object and then use methods on it (the SweepFeatureInput object) to define the sweep. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [sweepFeatures.add](sweepFeatures_add_Sample.htm) | Demonstrates the sweepFeatures.add method. |
| [Sweep Feature API Sample](SweepFeatureSample_Sample.htm) | Demonstrates creating a new sweep feature. |
| [Sweep with guide rail Feature API Sample](SweepWithGuideRailFeatureSample_Sample.htm) | Demonstrates creating a new Sweep feature that uses a guide rail along with a profile. |
| [Two Rail Sweep Feature API Sample](TwoRailSweepFeatureSample_Sample.htm) | Demonstrates creating new two rail sweep feature. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |