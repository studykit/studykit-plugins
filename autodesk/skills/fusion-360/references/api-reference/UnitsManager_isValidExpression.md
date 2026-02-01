# UnitsManager.isValidExpression Method

Parent Object: [UnitsManager](UnitsManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/UnitsManager.h>

## Description

Checks to see if the given expression is valid.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unitsManager\_var" is a variable referencing a [UnitsManager](UnitsManager.htm) object.```` ``` returnValue = unitsManager_var.isValidExpression(expression, units) ``` ```` |

"unitsManager\_var" is a variable referencing a [UnitsManager](UnitsManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns True if it is a valid expression. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| expression | string | The expression to validate. |
| units | string | The units to use when validating the expression. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |