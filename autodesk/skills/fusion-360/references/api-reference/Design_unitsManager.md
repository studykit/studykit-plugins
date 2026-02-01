# Design.unitsManager Property

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Returns the UnitsManager object associated with this product.

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a Design object. |

"design\_var" is a variable referencing a Design object. ```` ``` #include <Fusion/Fusion/Design.h>  // Get the value of the property. Ptr<UnitsManager> propertyValue = design_var->unitsManager(); ``` ```` |

## Property Value

This is a read only property whose value is a [UnitsManager](UnitsManager.htm).

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