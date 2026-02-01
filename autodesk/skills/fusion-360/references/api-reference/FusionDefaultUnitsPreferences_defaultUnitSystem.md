# FusionDefaultUnitsPreferences.defaultUnitSystem Property

Parent Object: [FusionDefaultUnitsPreferences](FusionDefaultUnitsPreferences.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionDefaultUnitsPreferences.h>

## Description

Gets and sets the default unit system when creating a new Fusion file.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionDefaultUnitsPreferences\_var" is a variable referencing a FusionDefaultUnitsPreferences object. |

"fusionDefaultUnitsPreferences\_var" is a variable referencing a FusionDefaultUnitsPreferences object. ```` ``` #include <Fusion/Fusion/FusionDefaultUnitsPreferences.h>  // Get the value of the property. UnitSystems propertyValue = fusionDefaultUnitsPreferences_var->defaultUnitSystem();  // Set the value of the property, where value_var is a UnitSystems. bool returnValue = fusionDefaultUnitsPreferences_var->defaultUnitSystem(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [UnitSystems](UnitSystems.htm).

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |