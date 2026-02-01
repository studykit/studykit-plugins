# UnitsManager.formatUnits Method

Parent Object: [UnitsManager](UnitsManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/UnitsManager.h>

## Description

Formats the unit according to the user preferences "centimeter" -> "cm" "inch" -> "in" "cm\* cm \*cm / s" -> , "cm^3 / s"

## Syntax

* [Python](#Python)
* [C++](#C++)

"unitsManager\_var" is a variable referencing a [UnitsManager](UnitsManager.htm) object.```` ``` returnValue = unitsManager_var.formatUnits(units) ``` ```` |

"unitsManager\_var" is a variable referencing a [UnitsManager](UnitsManager.htm) object. |

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