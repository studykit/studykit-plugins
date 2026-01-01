# OffsetConstraintInput.offset Property

Parent Object: [OffsetConstraintInput](OffsetConstraintInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/OffsetConstraintInput.h>

## Description

Gets and sets the value that defines the offset. This is a ValueInput object so it can be a float value to define the offset in centimeters or it can be a string defining an expression that will be used by the parameter controlling the offset. A positive offset value creates the offset curve to the "right" and a negative offset value goes to the "left".

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetConstraintInput\_var" is a variable referencing an OffsetConstraintInput object.  ```` ``` # Get the value of the property. propertyValue = offsetConstraintInput_var.offset  # Set the value of the property. offsetConstraintInput_var.offset = propertyValue ``` ```` |

"offsetConstraintInput\_var" is a variable referencing an OffsetConstraintInput object. ```` ``` #include <Fusion/Sketch/OffsetConstraintInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = offsetConstraintInput_var->offset();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = offsetConstraintInput_var->offset(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |