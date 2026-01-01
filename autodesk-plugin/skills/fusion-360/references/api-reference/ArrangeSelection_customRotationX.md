# ArrangeSelection.customRotationX Property

Parent Object: [ArrangeSelection](ArrangeSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ArrangeSelection.h>

## Description

Gets and sets the rotation increments (in degrees) for the x-axis. This function is not available in Fusion for Personal Use. Throws an exception when calling this function in Fusion for Personal Use. To enable any rotation the parameter "arrange\_rotation\_group" of the operation must be set to true. To disable x-axis rotation for this selection, customRotationX must be set to 0. The default value for this property is 45 degrees. Note: If customRotationX is called, isUsingCustomRotationX will be set to true automatically.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeSelection\_var" is a variable referencing an ArrangeSelection object. |

"arrangeSelection\_var" is a variable referencing an ArrangeSelection object. ```` ``` #include <Cam/GeometrySelections/ArrangeSelection.h>  // Get the value of the property. double propertyValue = arrangeSelection_var->customRotationX();  // Set the value of the property, where value_var is a double. bool returnValue = arrangeSelection_var->customRotationX(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |