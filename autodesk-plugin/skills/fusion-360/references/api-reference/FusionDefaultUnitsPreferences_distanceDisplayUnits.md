# FusionDefaultUnitsPreferences.distanceDisplayUnits Property

Parent Object: [FusionDefaultUnitsPreferences](FusionDefaultUnitsPreferences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionDefaultUnitsPreferences.h>

## Description

Gets and sets the default design units for length when creating a new Fusion file. Setting this property will have the side effect of changing the defaultUnitSystem property to custom.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionDefaultUnitsPreferences\_var" is a variable referencing a FusionDefaultUnitsPreferences object. |

"fusionDefaultUnitsPreferences\_var" is a variable referencing a FusionDefaultUnitsPreferences object. ```` ``` #include <Fusion/Fusion/FusionDefaultUnitsPreferences.h>  // Get the value of the property. DistanceUnits propertyValue = fusionDefaultUnitsPreferences_var->distanceDisplayUnits();  // Set the value of the property, where value_var is a DistanceUnits. bool returnValue = fusionDefaultUnitsPreferences_var->distanceDisplayUnits(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [DistanceUnits](DistanceUnits.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |