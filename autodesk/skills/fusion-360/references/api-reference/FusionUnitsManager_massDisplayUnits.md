# FusionUnitsManager.massDisplayUnits Property

Parent Object: [FusionUnitsManager](FusionUnitsManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionUnitsManager.h>

## Description

Gets and sets the default mass units for this design. Setting this property has the side effect of changing the unitSystem property to custom.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionUnitsManager\_var" is a variable referencing a FusionUnitsManager object. |

"fusionUnitsManager\_var" is a variable referencing a FusionUnitsManager object. ```` ``` #include <Fusion/Fusion/FusionUnitsManager.h>  // Get the value of the property. MassUnits propertyValue = fusionUnitsManager_var->massDisplayUnits();  // Set the value of the property, where value_var is a MassUnits. bool returnValue = fusionUnitsManager_var->massDisplayUnits(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [MassUnits](MassUnits.htm).

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |