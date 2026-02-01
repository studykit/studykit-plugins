# ArrangeSelection.isUsingCustomQuantity Property

Parent Object: [ArrangeSelection](ArrangeSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ArrangeSelection.h>

## Description

Gets and sets if custom quantity is used for this element. This function is not available in Fusion for Personal Use. Throws an exception when calling this function in Fusion for Personal Use. If isUsingCustomQuantity is false, the global quantity of the operation's parameter "arrange\_global\_quantity" is used. The default value for this property false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeSelection\_var" is a variable referencing an ArrangeSelection object. |

"arrangeSelection\_var" is a variable referencing an ArrangeSelection object. ```` ``` #include <Cam/GeometrySelections/ArrangeSelection.h>  // Get the value of the property. boolean propertyValue = arrangeSelection_var->isUsingCustomQuantity();  // Set the value of the property, where value_var is a boolean. bool returnValue = arrangeSelection_var->isUsingCustomQuantity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |