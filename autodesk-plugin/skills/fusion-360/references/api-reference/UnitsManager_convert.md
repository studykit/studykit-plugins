# UnitsManager.convert Method

Parent Object: [UnitsManager](UnitsManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/UnitsManager.h>

## Description

Converts a value from one unit to another. The input and output unit specifiers must be compatible. For example, "in" (inches) and "cm" (centimeters) will work because they both define length. So Convert(1.5, "in", "ft") -> 0.125 Convert(1.5, unitsManager.defaultLengthUnits, "cm") -> depends on the current default distance units, with "mm" it gives 0.15 So Convert(1.5, "in", "kg") -> -1 and GetLastError returns ExpressionError (to denote error) So Convert(1, "in", "internalUnits") -> 2.54 So Convert(1, "internalUnits", "in") -> 0.3937...

## Syntax

* [Python](#Python)
* [C++](#C++)

"unitsManager\_var" is a variable referencing a [UnitsManager](UnitsManager.htm) object.```` ``` returnValue = unitsManager_var.convert(valueInInputUnits, inputUnits, outputUnits) ``` ```` |

"unitsManager\_var" is a variable referencing a [UnitsManager](UnitsManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| double | Returns -1 AND GetLastError returns ExpressionError in the event of an error. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| valueInInputUnits | double | The value to convert |
| inputUnits | string | The units of the value to convert |
| outputUnits | string | The units to convert the value to |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |