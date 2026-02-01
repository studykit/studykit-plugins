# FusionUnitsManager.unitSystem Property

Parent Object: [FusionUnitsManager](FusionUnitsManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionUnitsManager.h>

## Description

Gets and sets the pre-defined combination of length and mass units to use for the units in the design. The distanceDisplayUnits and massDisplayUnits properties provide a way to get the current setting for distance and mass and to modify them to other values besides the predefined combinations. When a custom unit system is specified, any combination of distance and mass can be specified.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionUnitsManager\_var" is a variable referencing a FusionUnitsManager object. |

"fusionUnitsManager\_var" is a variable referencing a FusionUnitsManager object. ```` ``` #include <Fusion/Fusion/FusionUnitsManager.h>  // Get the value of the property. UnitSystems propertyValue = fusionUnitsManager_var->unitSystem();  // Set the value of the property, where value_var is a UnitSystems. bool returnValue = fusionUnitsManager_var->unitSystem(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [UnitSystems](UnitSystems.htm).

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |