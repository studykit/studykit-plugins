# MoveFeatureRotateDefinition.axisEntity Property

Parent Object: [MoveFeatureRotateDefinition](MoveFeatureRotateDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureRotateDefinition.h>

## Description

Gets and sets the linear entity that defines the axis of rotation. This can be a linear BRepEdge, ConstructionAxis, or a SketchLine. The natural direction of the entity defines a right-hand rule for the rotation direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatureRotateDefinition\_var" is a variable referencing a MoveFeatureRotateDefinition object.  ```` ``` # Get the value of the property. propertyValue = moveFeatureRotateDefinition_var.axisEntity  # Set the value of the property. moveFeatureRotateDefinition_var.axisEntity = propertyValue ``` ```` |

"moveFeatureRotateDefinition\_var" is a variable referencing a MoveFeatureRotateDefinition object. ```` ``` #include <Fusion/Features/MoveFeatureRotateDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = moveFeatureRotateDefinition_var->axisEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = moveFeatureRotateDefinition_var->axisEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |