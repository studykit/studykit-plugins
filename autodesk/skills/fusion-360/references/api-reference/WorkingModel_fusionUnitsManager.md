# WorkingModel.fusionUnitsManager Property

Parent Object: [WorkingModel](WorkingModel.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/WorkingModel.h>

## Description

Returns a specialized UnitsManager that can set the default length units and work with parameters.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workingModel\_var" is a variable referencing a WorkingModel object. |

"workingModel\_var" is a variable referencing a WorkingModel object. ```` ``` #include <Fusion/Fusion/WorkingModel.h>  // Get the value of the property. Ptr<FusionUnitsManager> propertyValue = workingModel_var->fusionUnitsManager(); ``` ```` |

## Property Value

This is a read only property whose value is a [FusionUnitsManager](FusionUnitsManager.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |