# OffsetConstraintInput.dimensionPoint Property

Parent Object: [OffsetConstraintInput](OffsetConstraintInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/OffsetConstraintInput.h>

## Description

A location on one of the curves where the offset dimension will be created. A value of null can be used to indicate that a default location should be used.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetConstraintInput\_var" is a variable referencing an OffsetConstraintInput object.  ```` ``` # Get the value of the property. propertyValue = offsetConstraintInput_var.dimensionPoint  # Set the value of the property. offsetConstraintInput_var.dimensionPoint = propertyValue ``` ```` |

"offsetConstraintInput\_var" is a variable referencing an OffsetConstraintInput object. ```` ``` #include <Fusion/Sketch/OffsetConstraintInput.h>  // Get the value of the property. Ptr<Point3D> propertyValue = offsetConstraintInput_var->dimensionPoint();  // Set the value of the property, where value_var is a Point3D. bool returnValue = offsetConstraintInput_var->dimensionPoint(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |