# ArrangeSelection.isUsingCustomRotationX Property

Parent Object: [ArrangeSelection](ArrangeSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ArrangeSelection.h>

## Description

Gets and sets if custom rotation is used for the x-axis. This function is not available in Fusion for Personal Use. Throws an exception when calling this function in Fusion for Personal Use. To enable any rotation the parameter "arrange\_rotation\_group" of the operation must be set to true. If isUsingCustomRotationX is false, the rotation of the operation's parameter "arrange\_rotation\_x" is used. The default value for this property false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeSelection\_var" is a variable referencing an ArrangeSelection object. |

"arrangeSelection\_var" is a variable referencing an ArrangeSelection object. ```` ``` #include <Cam/GeometrySelections/ArrangeSelection.h>  // Get the value of the property. boolean propertyValue = arrangeSelection_var->isUsingCustomRotationX();  // Set the value of the property, where value_var is a boolean. bool returnValue = arrangeSelection_var->isUsingCustomRotationX(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |