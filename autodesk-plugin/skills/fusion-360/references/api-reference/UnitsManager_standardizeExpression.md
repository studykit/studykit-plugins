# UnitsManager.standardizeExpression Method

Parent Object: [UnitsManager](UnitsManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/UnitsManager.h>

## Description

Standardizes the expression in terms of spacing and user preferences. StandardizeExpression("1.5") -> depends on distance units, but with might be "1.5 mm" StandardizeExpression("1.5", "in") -> "1.5 in" StandardizeExpression("1.5 cm + 1.50001 centimeter") -> "1.5 cm + 1.50001 cm" StandardizeExpression("1.5", "m \* m \* m / s") -> "1.5 m^3 /s"

## Syntax

* [Python](#Python)
* [C++](#C++)

"unitsManager\_var" is a variable referencing a [UnitsManager](UnitsManager.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"unitsManager\_var" is a variable referencing a [UnitsManager](UnitsManager.htm) object.  ```` ``` #include <Core/Application/UnitsManager.h>  // Uses no optional arguments. returnValue = unitsManager_var->standardizeExpression(expression);  // Uses optional arguments. returnValue = unitsManager_var->standardizeExpression(expression, units); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string | Returns an empty string AND GetLastError returns ExpressionError in the event of an error. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| expression | string | The expression to standardize |
| units | string | The units to apply to the standardized expression. If not supplied the units will default to the default length specified in the preferences.   This is an optional argument whose default value is "DefaultDistance". |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |