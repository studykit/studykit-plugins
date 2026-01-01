# MoveFeatureFreeMoveDefinition.transform Property

Parent Object: [MoveFeatureFreeMoveDefinition](MoveFeatureFreeMoveDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureFreeMoveDefinition.h>

## Description

Gets and sets the transform that's applied to the face or body. The matrix must be an orthogonal matrix; that is the axes are perpendicular to each other and there isn't any scaling or mirroring defined.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatureFreeMoveDefinition\_var" is a variable referencing a MoveFeatureFreeMoveDefinition object.  ```` ``` # Get the value of the property. propertyValue = moveFeatureFreeMoveDefinition_var.transform  # Set the value of the property. moveFeatureFreeMoveDefinition_var.transform = propertyValue ``` ```` |

"moveFeatureFreeMoveDefinition\_var" is a variable referencing a MoveFeatureFreeMoveDefinition object. ```` ``` #include <Fusion/Features/MoveFeatureFreeMoveDefinition.h>  // Get the value of the property. Ptr<Matrix3D> propertyValue = moveFeatureFreeMoveDefinition_var->transform();  // Set the value of the property, where value_var is a Matrix3D. bool returnValue = moveFeatureFreeMoveDefinition_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix3D](Matrix3D.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |