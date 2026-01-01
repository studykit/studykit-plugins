# SweepFeatureInput.profile Property

Parent Object: [SweepFeatureInput](SweepFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SweepFeatureInput.h>

## Description

Gets and sets the profiles or planar faces used to define the shape of the sweep. This property can return or be set with a single Profile, a single planar face, or an ObjectCollection consisting of multiple profiles and planar faces. When an ObjectCollection is used all of the profiles and faces must be co-planar.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. |

"sweepFeatureInput\_var" is a variable referencing a SweepFeatureInput object. ```` ``` #include <Fusion/Features/SweepFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = sweepFeatureInput_var->profile();  // Set the value of the property, where value_var is a Base. bool returnValue = sweepFeatureInput_var->profile(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sweep with guide rail Feature API Sample](SweepWithGuideRailFeatureSample_Sample.htm) | Demonstrates creating a new Sweep feature that uses a guide rail along with a profile. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |