# SweepFeatureInput.orientation Property

Parent Object: [SweepFeatureInput](SweepFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatureInput.h>

## Description

Gets and sets the sweep orientation. It defaults to PerpendicularOrientationType. This property is ignored when sweeping a solid or a guide rail or surface has been specified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. |

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. ```` ``` #include <Fusion/Features/SweepFeatureInput.h>  // Get the value of the property. SweepOrientationTypes propertyValue = sweepFeatureInput_var->orientation();  // Set the value of the property, where value_var is a SweepOrientationTypes. bool returnValue = sweepFeatureInput_var->orientation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SweepOrientationTypes](SweepOrientationTypes.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [sweepFeatures.add](sweepFeatures_add_Sample.htm) | Demonstrates the sweepFeatures.add method. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |