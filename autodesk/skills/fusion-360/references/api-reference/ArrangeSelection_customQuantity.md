# ArrangeSelection.customQuantity Property

Parent Object: [ArrangeSelection](ArrangeSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ArrangeSelection.h>

## Description

Gets and sets the custom quantity. This function is not available in Fusion for Personal Use. Throws an exception when calling this function in Fusion for Personal Use. The default value for this property is 1. Note: If customQuantity is called, isUsingCustomQuantity will be set to true automatically.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeSelection\_var" is a variable referencing an ArrangeSelection object. |

"arrangeSelection\_var" is a variable referencing an ArrangeSelection object. ```` ``` #include <Cam/GeometrySelections/ArrangeSelection.h>  // Get the value of the property. uinteger propertyValue = arrangeSelection_var->customQuantity();  // Set the value of the property, where value_var is a uinteger. bool returnValue = arrangeSelection_var->customQuantity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a uinteger.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |