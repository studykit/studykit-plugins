# Design.fusionUnitsManager Property

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Returns a specialized UnitsManager that can set the default length units and work with parameters.

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a Design object. |

"design\_var" is a variable referencing a Design object. ```` ``` #include <Fusion/Fusion/Design.h>  // Get the value of the property. Ptr<FusionUnitsManager> propertyValue = design_var->fusionUnitsManager(); ``` ```` |

## Property Value

This is a read only property whose value is a [FusionUnitsManager](FusionUnitsManager.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |