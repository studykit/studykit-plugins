# MoveFeature.transform Property

Parent Object: [MoveFeature](MoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeature.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property is obsolete. The move feature now supports more than a simple transform. This property can still work in the case where a move feature was created using the FreeMove type of move but will fail in all other cases.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeature\_var" is a variable referencing a MoveFeature object.  ```` ``` # Get the value of the property. propertyValue = moveFeature_var.transform  # Set the value of the property. moveFeature_var.transform = propertyValue ``` ```` |

"moveFeature\_var" is a variable referencing a MoveFeature object. ```` ``` #include <Fusion/Features/MoveFeature.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = moveFeature_var->transform();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = moveFeature_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version March 2015
Retired in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |