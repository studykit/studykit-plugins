# SweepFeatureInput.isDirectionFlipped Property

Parent Object: [SweepFeatureInput](SweepFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatureInput.h>

## Description

Gets and sets if the direction of the sweep is flipped. This property only applies to sweep features that include a guide rail and whose path runs on both sides of the profile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. |

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. ```` ``` #include <Fusion/Features/SweepFeatureInput.h>  // Get the value of the property. boolean propertyValue = sweepFeatureInput_var->isDirectionFlipped();  // Set the value of the property, where value_var is a boolean. bool returnValue = sweepFeatureInput_var->isDirectionFlipped(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Two Rail Sweep Feature API Sample](TwoRailSweepFeatureSample_Sample.htm) | Demonstrates creating new two rail sweep feature. |

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |