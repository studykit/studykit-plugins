# MoveFeatureInput.transform Property

Parent Object: [MoveFeatureInput](MoveFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureInput.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property is obsolete. You should now use the setToFreeMove for the equivalent functionality.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatureInput\_var" is a variable referencing a MoveFeatureInput object.  ```` ``` # Get the value of the property. propertyValue = moveFeatureInput_var.transform  # Set the value of the property. moveFeatureInput_var.transform = propertyValue ``` ```` |

"moveFeatureInput\_var" is a variable referencing a MoveFeatureInput object. ```` ``` #include <Fusion/Features/MoveFeatureInput.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = moveFeatureInput_var->transform();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = moveFeatureInput_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version March 2015
Retired in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |