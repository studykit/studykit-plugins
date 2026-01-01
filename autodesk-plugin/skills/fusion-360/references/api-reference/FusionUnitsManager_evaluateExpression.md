# FusionUnitsManager.evaluateExpression Method

Parent Object: [FusionUnitsManager](FusionUnitsManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionUnitsManager.h>

## Description

Gets the value (in internal units) of the expression.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionUnitsManager\_var" is a variable referencing a [FusionUnitsManager](FusionUnitsManager.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"fusionUnitsManager\_var" is a variable referencing a [FusionUnitsManager](FusionUnitsManager.htm) object.  ```` ``` #include <Fusion/Fusion/FusionUnitsManager.h>  // Uses no optional arguments. returnValue = fusionUnitsManager_var->evaluateExpression(expression);  // Uses optional arguments. returnValue = fusionUnitsManager_var->evaluateExpression(expression, units); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| double | Returns -1 AND GetLastError will return ExpressionError in the event of an error. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| expression | string | EvaluateExpression("1cm + 1in") -> 3.54 EvaluateExpression("1") -> -> depends on the DistanceUnits, with "mm" it gives 0.1 |
| units | string | If not supplied the units will default to the default length specified in the preferences.   This is an optional argument whose default value is "DefaultDistance". |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |