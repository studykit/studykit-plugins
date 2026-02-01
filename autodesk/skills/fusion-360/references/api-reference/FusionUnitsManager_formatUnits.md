# FusionUnitsManager.formatUnits Method

Parent Object: [FusionUnitsManager](FusionUnitsManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionUnitsManager.h>

## Description

Formats the unit according to the user preferences "centimeter" -> "cm" "inch" -> "in" "cm\* cm \*cm / s" -> , "cm^3 / s"

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionUnitsManager\_var" is a variable referencing a [FusionUnitsManager](FusionUnitsManager.htm) object.```` ``` returnValue = fusionUnitsManager_var.formatUnits(units) ``` ```` |

"fusionUnitsManager\_var" is a variable referencing a [FusionUnitsManager](FusionUnitsManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string | Returns an empty string and GetLastError returns ExpressionError in the event of an error. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| units | string | The unit to use when converting the value into a string. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |