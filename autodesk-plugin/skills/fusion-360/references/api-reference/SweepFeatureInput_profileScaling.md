# SweepFeatureInput.profileScaling Property

Parent Object: [SweepFeatureInput](SweepFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatureInput.h>

## Description

Gets and sets the sweep profile scaling option. It defaults to SweepProfileScaleOption. This property is only used when a guide rail has been specified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. |

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. ```` ``` #include <Fusion/Features/SweepFeatureInput.h>  // Get the value of the property. SweepProfileScalingOptions propertyValue = sweepFeatureInput_var->profileScaling();  // Set the value of the property, where value_var is a SweepProfileScalingOptions. bool returnValue = sweepFeatureInput_var->profileScaling(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SweepProfileScalingOptions](SweepProfileScalingOptions.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sweep with guide rail Feature API Sample](SweepWithGuideRailFeatureSample_Sample.htm) | Demonstrates creating a new Sweep feature that uses a guide rail along with a profile. |
| [Two Rail Sweep Feature API Sample](TwoRailSweepFeatureSample_Sample.htm) | Demonstrates creating new two rail sweep feature. |

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |