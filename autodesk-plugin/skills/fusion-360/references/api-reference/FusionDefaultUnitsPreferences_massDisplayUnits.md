# FusionDefaultUnitsPreferences.massDisplayUnits Property

Parent Object: [FusionDefaultUnitsPreferences](FusionDefaultUnitsPreferences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionDefaultUnitsPreferences.h>

## Description

Gets and sets the default design units for mass when creating a new Fusion file. Setting this property will have the side effect of changing the defaultUnitSystem property to custom.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionDefaultUnitsPreferences\_var" is a variable referencing a FusionDefaultUnitsPreferences object. |

"fusionDefaultUnitsPreferences\_var" is a variable referencing a FusionDefaultUnitsPreferences object. ```` ``` #include <Fusion/Fusion/FusionDefaultUnitsPreferences.h>  // Get the value of the property. MassUnits propertyValue = fusionDefaultUnitsPreferences_var->massDisplayUnits();  // Set the value of the property, where value_var is a MassUnits. bool returnValue = fusionDefaultUnitsPreferences_var->massDisplayUnits(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MassUnits](MassUnits.htm).

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |