# SetupInput.stockMode Property

Parent Object: [SetupInput](SetupInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupInput.h>

## Description

StockMode for the setup.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupInput\_var" is a variable referencing a SetupInput object. |

"setupInput\_var" is a variable referencing a SetupInput object. ```` ``` #include <Cam/CAM/SetupInput.h>  // Get the value of the property. SetupStockModes propertyValue = setupInput_var->stockMode();  // Set the value of the property, where value_var is a SetupStockModes. bool returnValue = setupInput_var->stockMode(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SetupStockModes](SetupStockModes.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |