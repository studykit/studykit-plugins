# UnitsManager.evaluateExpression Method

Parent Object: [UnitsManager](UnitsManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/UnitsManager.h>

## Description

Gets the value (in internal units) of the expression.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unitsManager\_var" is a variable referencing a [UnitsManager](UnitsManager.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"unitsManager\_var" is a variable referencing a [UnitsManager](UnitsManager.htm) object.  ```` ``` #include <Core/Application/UnitsManager.h>  // Uses no optional arguments. returnValue = unitsManager_var->evaluateExpression(expression);  // Uses optional arguments. returnValue = unitsManager_var->evaluateExpression(expression, units); ``` ```` |

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

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Use inputBox to get value and evaluateExpression to validate it](InputBox_Sample.htm) | Uses the UserInterface.inputBox function to get a string from the user and then validates that the strinng entered is a valid expression by using the UnitsManager.evaluateExpression function. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |